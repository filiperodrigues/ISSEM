# coding:utf-8
from django.http import Http404
from django.shortcuts import render
from issem.models import ServidorModel
from issem.forms import ServidorFormCad, ServidorFormEdit
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group
from issem.views.pagination import pagination
from django.contrib.auth.models import User
from django.db.models import Q


class ServidorView(View):
    template = 'cruds/servidor.html'
    template_lista = 'listas/servidores.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo') or user.groups.filter(name='Tecnico')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}
        if id:  # EDIÇÃO
            try:
                servidor = ServidorModel.objects.get(pk=id, excluido=False)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
                administrador = ServidorModel.objects.get(id=request.user.id).administrador
                context_dict['administrador'] = administrador
                context_dict['crm'] = servidor.crm
            except:
                raise Http404("Servidor não encontrado.")
            form = ServidorFormEdit(instance=servidor, id=id)
            try:
                group_user = Group.objects.get(user=id)
                context_dict['grupo'] = group_user
            except:
                raise Http404("Grupo do usuário não encontrado.")
            id_group_user = group_user.id
        else:  # CADASTRO NOVO
            form = ServidorFormCad()  # MODO CADASTRO: recebe o formulário vazio
            id_group_user = ""


        context_dict['method'] = 'get'
        context_dict['form'] = form
        context_dict['id'] = id
        context_dict['id_group_user'] = id_group_user
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template, context_dict)

    # TODO: REFATORAR
    @method_decorator(user_passes_test(group_test))
    def post(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}
        id_group_user = None
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            try:
                servidor = ServidorModel.objects.get(pk=id, excluido=False)
            except:
                raise Http404("Servidor não encontrado.")
            form = ServidorFormEdit(instance=servidor, data=request.POST, id=id)
            try:
                group_user = Group.objects.get(user=id)
                context_dict['grupo'] = group_user
            except:
                raise Http404("Grupo do usuário não encontrado.")
            id_group_user = group_user.id

            if form.is_valid():
                form.save(commit=False)
                servidor.save()

                msg = 'Alterações realizadas com sucesso!'
                tipo_msg = 'green'
            else:
                print(form.errors)
                msg = 'Erros encontrados!'
                tipo_msg = 'red'

        else:  # CADASTRO NOVO
            id = None
            form = ServidorFormCad(data=request.POST)

            if form.is_valid():
                form.save()
                if id != None:
                    if Group.objects.get(user=id):
                        group_name = Group.objects.get(user=id)
                        group_name.user_set.remove(id)

                gp = Group.objects.get(id=request.POST["groups"])
                user = ServidorModel.objects.get(username=request.POST["username"])
                user.groups.add(gp)
                user.save()
                msg = 'Cadastro efetuado com sucesso!'
                tipo_msg = 'green'
                form = ServidorFormCad()
            else:
                print(form.errors)
                msg = 'Erros encontrados!'
                tipo_msg = 'red'

        context_dict['form'] = form
        context_dict['id'] = id
        context_dict['id_group_user'] = id_group_user
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template, context_dict)

    @classmethod
    def ServidorDelete(self, request, id):
        try:
            servidor = ServidorModel.objects.get(pk=id)
        except:
            raise Http404("Servidor não encontrado.")
        servidor.excluido = True
        servidor.is_active = False
        servidor.save()
        msg = "Servidor excluído com sucesso!"
        tipo_msg = "green"
        return self.ListaServidores(request, msg, tipo_msg)

    @classmethod
    def ListaServidores(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        if request.GET:
            ''' SE EXISTIR PAGINAÇÃO OU FILTRO; CASO EXISTA FILTRO MAS NÃO EXISTA PAGINAÇÃO,
            FARÁ A PAGINAÇÃO COM VALOR IGUAL À ZERO '''
            if request.POST and 'filtro_grupo' in request.POST:
                if 'filtro' in request.GET:
                    if request.POST['filtro_grupo'] != "todos":
                        if request.POST['filtro_grupo'] == "administrativo":
                            id_grupo = Group.objects.get(name="Administrativo").id
                        elif request.POST['filtro_grupo'] == "tecnico":
                            id_grupo = Group.objects.get(name="Tecnico").id
                        else:
                            raise Http404("Ocorreu algum erro, verifique e tente novamente!")
                        servidores = ServidorModel.objects.filter(
                            Q(cpf__icontains=request.GET.get('filtro'), excluido=False, groups=id_grupo) |
                            Q(nome__icontains=request.GET.get('filtro'), excluido=False, groups=id_grupo) |
                            Q(email__icontains=request.GET.get('filtro'), excluido=False, groups=id_grupo)).order_by('nome')
                    else:
                        servidores = ServidorModel.objects.filter(
                            Q(cpf__icontains=request.GET.get('filtro'), excluido=False) |
                            Q(nome__icontains=request.GET.get('filtro'), excluido=False) |
                            Q(email__icontains=request.GET.get('filtro'), excluido=False)).order_by('nome')
                else:
                    if request.POST['filtro_grupo'] != "todos":
                        if request.POST['filtro_grupo'] == "administrativo":
                            id_grupo = Group.objects.get(name="Administrativo").id
                        elif request.POST['filtro_grupo'] == "tecnico":
                            id_grupo = Group.objects.get(name="Tecnico").id
                        else:
                            raise Http404("Ocorreu algum erro, verifique e tente novamente!")
                        servidores = ServidorModel.objects.filter(excluido=False, groups=id_grupo)
                    else:
                        servidores = ServidorModel.objects.filter(excluido=False)
            else:
                if 'filtro' in request.GET:
                    servidores = ServidorModel.objects.filter(
                        Q(cpf__icontains=request.GET.get('filtro'), excluido=False) |
                        Q(nome__icontains=request.GET.get('filtro'), excluido=False) |
                        Q(email__icontains=request.GET.get('filtro'), excluido=False)).order_by('nome')
                else:
                    servidores = ServidorModel.objects.filter(excluido=False)
        else:
            if request.POST and 'filtro_grupo' in request.POST:
                if request.POST['filtro_grupo'] == "todos":
                    servidores = ServidorModel.objects.filter(excluido=False)
                elif request.POST['filtro_grupo'] == "administrativo":
                    servidores = ServidorModel.objects.filter(excluido=False,
                                                              groups=Group.objects.get(name="Administrativo").id)
                elif request.POST['filtro_grupo'] == "tecnico":
                    servidores = ServidorModel.objects.filter(excluido=False,
                                                              groups=Group.objects.get(name="Tecnico").id)
                else:
                    raise Http404("Ocorreu algum erro, verifique e tente novamente!")
            else:
                servidores = ServidorModel.objects.filter(excluido=False).order_by('nome')

        dados, page_range, ultima = pagination(servidores, request.GET.get('page'))
        usuario_logado = User.objects.get(pk=request.user.id)
        if not request.user.is_superuser:
            administrador = ServidorModel.objects.get(pk=request.user.id).administrador
        else:
            administrador = 0

        context_dict['grupo_controle'] = request.POST['filtro_grupo'] if request.POST else ""
        context_dict['dados'] = dados
        context_dict['page_range'] = page_range
        context_dict['ultima'] = ultima
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        context_dict['filtro'] = request.GET.get('filtro')
        context_dict['usuario_logado'] = usuario_logado
        context_dict['administrador'] = administrador
        return render(request, self.template_lista, context_dict)
