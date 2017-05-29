# coding:utf-8
from django.http import Http404
from django.shortcuts import render
from issem.models import SeguradoModel, RequerimentoModel, DependenteModel
from issem.forms import PessoaPasswordForm, SeguradoFormEdit, SeguradoFormCad
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group
from issem.views.pagination import pagination


class SeguradoView(View):
    template = 'cruds/segurado.html'
    template_lista = 'listas/segurados.html'
    template_lista_segurados = 'listas/requerimentos_segurado.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo') or user.groups.filter(name='Segurado')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}

        if id:
            try:
                segurado = SeguradoModel.objects.get(pk=id, excluido=0)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
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
                segurado = SeguradoModel.objects.get(pk=id, excluido=0)
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
                    user = SeguradoModel.objects.get(username=request.POST["username"])
                    user.groups.add(gp)
                    user.save()
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
        return render(request, self.template, context_dict)

    @classmethod
    def SeguradoDelete(self, request, id=None):
        try:
            segurado = SeguradoModel.objects.get(pk=id)
        except:
            raise Http404("Segurado não encontrado.")

        #REMOVE TODOS OS DEPENDENTES DO SEGURADO
        for dependente in segurado.dependente.all():
            dp = DependenteModel.objects.get(pk=dependente.id)
            dp.excluido = True
            dp.is_active = False
            dp.save()
            print(dp)
        segurado.excluido = True
        segurado.is_active = False
        segurado.save()
        msg = "Segurado excluído com sucesso!"
        tipo_msg = "green"
        return self.ListaSegurados(request, msg, tipo_msg)

    @classmethod
    def ListaSegurados(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        if request.GET or 'page' in request.GET:
            if request.GET.get('filtro'):
                segurado1 = SeguradoModel.objects.filter(cpf__icontains=request.GET.get('filtro'), excluido=0)
                segurado2 = SeguradoModel.objects.filter(nome__icontains=request.GET.get('filtro'), excluido=0)
                segurado3 = SeguradoModel.objects.filter(email__icontains=request.GET.get('filtro'), excluido=0)
                segurados = list(segurado1) + list(segurado2) + list(segurado3)
                segurados = list(set(segurados))
            else:
                segurados = SeguradoModel.objects.filter(excluido=False)
        else:
            segurados = SeguradoModel.objects.filter(excluido=False)

        dados, page_range, ultima = pagination(segurados, request.GET.get('page'))
        context_dict['dados'] = dados
        context_dict['page_range'] = page_range
        context_dict['ultima'] = ultima
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        context_dict['filtro'] = request.GET.get('filtro')
        return render(request, self.template_lista, context_dict)

    @classmethod
    def ListaRequerimentosSegurado(self, request, id=None):
        context_dict = {}
        requerimentos = RequerimentoModel.objects.filter(segurado=id)
        dados, page_range, ultima = pagination(requerimentos, request.GET.get('page'))
        context_dict['dados'] = dados
        context_dict['page_range'] = page_range
        context_dict['ultima'] = ultima
        return render(request, self.template_lista_segurados, context_dict)
