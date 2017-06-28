# coding:utf-8
from django.http import Http404, request
from django.shortcuts import render
from issem.models import SeguradoModel, DependenteModel, ParametrosConfiguracaoModel
from issem.forms import SeguradoFormEdit, SeguradoFormCad
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group, User
from issem.models import ServidorModel
from issem.views.pagination import pagination
from django.db.models import Q
import string
import random
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator


class SeguradoView(View):
    template = 'cruds/segurado.html'
    template_lista = 'listas/segurados.html'
    template_inativos = 'listas/segurados_inativos.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo') or user.groups.filter(name='Segurado')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}
        if str(request.user.groups.all()[0]) == "Administrativo":
            administrador = ServidorModel.objects.get(pk=request.user.id).administrador
            context_dict['administrador'] = administrador

        if id:
            try:
                segurado = SeguradoModel.objects.get(pk=id,
                                                     excluido=False)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
                context_dict['id_segurado'] = segurado.id
            except:
                raise Http404("Segurado não encontrado.")
            form = SeguradoFormEdit(instance=segurado, id=id)
            try:
                group_user = Group.objects.get(user=id)
            except:
                raise Http404("Grupo do usuário não encontrado.")
            id_group_user = group_user.id
        else:
            form = SeguradoFormCad()  # MODO CADASTRO: recebe o formulário vazio
            id_group_user = ""

        context_dict['form'] = form
        context_dict['id'] = id
        context_dict['id_group_user'] = id_group_user
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        context_dict['usuario_logado'] = User.objects.get(pk=request.user.id).id
        return render(request, self.template, context_dict)

    def post(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}
        valido = False
        id_group_user = None
        user_id = None
        user_nome = None

        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            try:
                segurado = SeguradoModel.objects.get(pk=id, excluido=False)
            except:
                raise Http404("Segurado não encontrado.")
            form = SeguradoFormEdit(instance=segurado, data=request.POST, id=id)
            try:
                group_user = Group.objects.get(user=id)
            except:
                raise Http404("Grupo do usuário não encontrado.")
            id_group_user = group_user.id

            if form.is_valid():
                form.save()
                msg = 'Alterações realizadas com sucesso!'
                tipo_msg = 'green'
                valido = True
        else:  # CADASTRO NOVO
            form = SeguradoFormCad(data=request.POST)

            if form.is_valid():
                form.save()

                try:
                    gp = Group.objects.get(name='Segurado')
                    user = SeguradoModel.objects.get(email=request.POST["email"])

                    # Define uma senha aleatória para o Segurado e seta o e-mail inserido como "username"
                    user.username = form.data.get('email')
                    user.groups.add(gp)
                    user.primeiro_login = True
                    user.save()

                    #Token link segurado
                    token = default_token_generator.make_token(user)
                    uid = urlsafe_base64_encode(force_bytes(user.pk))

                    EnviaEmailSenha(user.username, token, uid)

                except:
                    raise Http404("Ocorreu algum erro, verifique e tente novamente.")

                msg = "Cadastro efetuado com sucesso!"
                tipo_msg = 'green'
                form = SeguradoFormCad()
                valido = True
                user_id = user.id
                user_nome = user.nome

        if not valido:
            print(form.errors)
            msg = 'Erros encontrados!'
            tipo_msg = 'red'

        context_dict['form'] = form
        context_dict['id'] = id
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        context_dict['id_segurado'] = user_id
        context_dict['nome'] = user_nome
        context_dict['id_group_user'] = id_group_user
        context_dict['usuario_logado'] = User.objects.get(pk=request.user.id).id
        return render(request, self.template, context_dict)

    @classmethod
    def SeguradoDelete(self, request, id=None):
        try:
            segurado = SeguradoModel.objects.get(pk=id)
        except:
            raise Http404("Segurado não encontrado.")

        # REMOVE TODOS OS DEPENDENTES DO SEGURADO
        for dependente in segurado.dependente.all():
            dp = DependenteModel.objects.get(pk=dependente.id)
            dp.excluido = True
            dp.is_active = False
            dp.save()
        segurado.excluido = True
        segurado.is_active = False
        segurado.save()
        msg = "Segurado excluído com sucesso!"
        tipo_msg = "green"
        return self.ListaSegurados(request, msg, tipo_msg)

    @classmethod
    def SeguradoAtiva(self, request, id=None):
        try:
            segurado = SeguradoModel.objects.get(pk=id)
        except:
            raise Http404("Segurado não encontrado.")

        # REMOVE TODOS OS DEPENDENTES DO SEGURADO
        for dependente in segurado.dependente.all():
            dp = DependenteModel.objects.get(pk=dependente.id)
            dp.excluido = False
            dp.is_active = True
            dp.save()
        segurado.excluido = False
        segurado.is_active = True
        segurado.save()
        msg = "Segurado excluído com sucesso!"
        tipo_msg = "green"
        return self.ListaSegurados(request, msg, tipo_msg)

    @classmethod
    def ListaSegurados(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        if request.GET:
            ''' SE EXISTIR PAGINAÇÃO OU FILTRO; CASO EXISTA FILTRO MAS NÃO EXISTA PAGINAÇÃO,
            FARÁ A PAGINAÇÃO COM VALOR IGUAL À ZERO '''
            if 'filtro' in request.GET:
                segurados = SeguradoModel.objects.filter(
                    Q(cpf__icontains=request.GET.get('filtro'), excluido=False) |
                    Q(nome__icontains=request.GET.get('filtro'), excluido=False) |
                    Q(email__icontains=request.GET.get('filtro'), excluido=False)).order_by('nome')
            else:
                segurados = SeguradoModel.objects.filter(excluido=False)
        else:
            segurados = SeguradoModel.objects.filter(excluido=False).order_by('nome')

        if not request.user.is_superuser:
            administrador = ServidorModel.objects.get(pk=request.user.id).administrador
        else:
            administrador = 0

        dados, page_range, ultima = pagination(segurados, request.GET.get('page'))
        context_dict['dados'] = dados
        context_dict['page_range'] = page_range
        context_dict['ultima'] = ultima
        context_dict['administrador'] = administrador
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        context_dict['filtro'] = request.GET.get('filtro')
        return render(request, self.template_lista, context_dict)

    @classmethod
    def ListaSeguradosInativos(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        if request.GET:
            ''' SE EXISTIR PAGINAÇÃO OU FILTRO; CASO EXISTA FILTRO MAS NÃO EXISTA PAGINAÇÃO,
            FARÁ A PAGINAÇÃO COM VALOR IGUAL À ZERO '''
            if 'filtro' in request.GET:
                segurados = SeguradoModel.objects.filter(
                    Q(cpf__icontains=request.GET.get('filtro'), excluido=True) |
                    Q(nome__icontains=request.GET.get('filtro'), excluido=True) |
                    Q(email__icontains=request.GET.get('filtro'), excluido=True)).order_by('nome')
            else:
                segurados = SeguradoModel.objects.filter(excluido=True)

        else:
            segurados = SeguradoModel.objects.filter(excluido=True).order_by('nome')

        if not request.user.is_superuser:
            administrador = ServidorModel.objects.get(pk=request.user.id).administrador
        else:
            administrador = 0

        dados, page_range, ultima = pagination(segurados, request.GET.get('page'))
        context_dict['dados'] = dados
        context_dict['page_range'] = page_range
        context_dict['ultima'] = ultima
        context_dict['administrador'] = administrador
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        context_dict['filtro'] = request.GET.get('filtro')
        return render(request, self.template_inativos, context_dict)


def EnviaEmailSenha(username, token, uid):
    segurado = SeguradoModel.objects.get(username=username)
    parametros_configuracoes = ParametrosConfiguracaoModel.objects.all().last()
    if (segurado.email):
        msg_topo = (
        "Prezado(a) senhor(a) <st3rong>" + segurado.nome + "</strong>, você foi cadastrado no Sistema ISSEM. Segue o link para acesso ao Sistema:<br/><br/>")
        link = "<a href='http://127.0.0.1:8000/issem/primeiro_login/%s/%s/'><font size='3'><strong>Acesse sua conta<strong></font></a>"%(uid, token)
        msg_rodape = "<h4>----</h4>" \
                     "<font size='5'><strong>ISSEM<strong></font><br/>" \
                     "<strong>Instituto de Seguridade do Servidores Municipais</strong><br/>" \
                     "Contato: " + str(parametros_configuracoes.telefone_issem) + "<br/>" \
                                                                                  "<br/><span style='color:red'><em>Obs: Este e-mail foi gerado pelo Sistema ISSEM, respostas não serão consideradas</em></span>"

        msg_completa_email = str(msg_topo + link + msg_rodape)
        email = EmailMultiAlternatives(
            'Informações de Cadastro - ISSEM',
            msg_completa_email,
            'ISSEM - Instituto de Seguridade dos Servidores Municipais',
            [str(segurado.email)],

        )
        email.attach_alternative(msg_completa_email, "text/html")
        email.send()
    return ""


def VerificaTokenPrimeiroLoginSegurado(request, uidb64, token):
    print("uidb64", uidb64)
    print("token", token)
    if uidb64 is not None and token is not None:
        uid = urlsafe_base64_decode(uidb64)
        user = SeguradoModel.objects.get(pk=uid)
        grupo = user.groups.get()
        if default_token_generator.check_token(user, token):
            return HttpResponseRedirect(reverse('issem:edita_senha', args=(user.id, grupo.id)))

    return HttpResponseRedirect(reverse('issem:index'))

