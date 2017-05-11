# coding:utf-8
from django.http import Http404
from django.shortcuts import render
from issem.models import DependenteModel, SeguradoModel
from issem.forms import DependenteFormCad, DependenteFormEdit
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group
from issem.views.pagination import pagination
from issem.views.cruds.pass_generator import mkpass


class DependenteView(View):
    template = 'cruds/dependente.html'
    template_lista = 'listas/dependentes.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id=None, id_segurado=None, msg=None, tipo_msg=None):
        context_dict = {}
        segurado = None
        id_group_user = None

        if id:
            try:
                dependente = DependenteModel.objects.get(pk=id)
                # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            except:
                raise Http404("Dependente não encontrado.")
            try:
                segurado = SeguradoModel.objects.get(dependente__id=id)
            except:
                segurado = None
            form = DependenteFormEdit(instance=dependente)
            try:
                id_group_user = Group.objects.get(user=id).id
            except:
                raise Http404("Ocorreu algum erro, verifique e tente novamente.")
        else:
            if id_segurado:
                try:
                    segurado = SeguradoModel.objects.get(pk=id_segurado)
                except:
                    raise Http404("Segurado deste dependente não encontrado.")
            form = DependenteFormCad()  # MODO CADASTRO: recebe o formulário vazio

        context_dict['form'] = form
        context_dict['id'] = id
        context_dict['id_group_user'] = id_group_user
        context_dict['segurado'] = segurado
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template, context_dict)

    def post(self, request, id_segurado=None, msg=None, tipo_msg=None):
        context_dict = {}
        valido = False
        id_group_user = None
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            try:
                dependente = DependenteModel.objects.get(pk=id)
            except:
                raise Http404("Dependente não encontrado.")
            try:
                segurado = SeguradoModel.objects.get(dependente=dependente)
            except:
                segurado = None
            form = DependenteFormEdit(instance=dependente, data=request.POST)
            try:
                id_group_user = Group.objects.get(user=id).id
            except:
                raise Http404("Ocorreu algum erro, verifique e tente novamente.")
            if form.is_valid():
                form.save()
                msg = 'Alterações realizadas com sucesso!'
                tipo_msg = 'green'
                valido = True

        else:  # CADASTRO NOVO
            id = None
            id_segurado = request.POST['id_segurado']
            try:
                segurado = SeguradoModel.objects.get(pk=id_segurado)
            except:
                segurado = None
            form = DependenteFormCad(data=request.POST)

            if form.is_valid():
                form.save()
                try:
                    gp = Group.objects.get(name='Dependente')
                    user = DependenteModel.objects.get(username=request.POST["username"])
                    user.groups.add(gp)
                    user.is_active = False
                    user.set_password(mkpass())
                    user.username = user.cpf
                    user.save()
                except:
                    raise Http404("Ocorreu algum erro, verifique e tente novamente.")
                user.groups.add(gp)
                user.is_active = False
                user.set_password(mkpass())
                user.username = user.cpf
                user.save()
                if segurado:
                    segurado.dependente.add(user)
                    segurado.save()
                msg = 'Cadastro efetuado com sucesso!'
                tipo_msg = 'green'
                form = DependenteFormCad()
                valido = True

        if not valido:
            print(form.errors)
            msg = 'Erros encontrados!'
            tipo_msg = 'red'

        context_dict['form'] = form
        context_dict['id'] = id
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        context_dict['segurado'] = segurado
        context_dict['id_group_user'] = id_group_user
        context_dict['dependente'] = True
        return render(request, self.template, context_dict)

    @classmethod
    def DependenteDelete(self, request, id):
        try:
            dependente = DependenteModel.objects.get(pk=id)
        except:
            raise Http404("Dependente não encontrado.")
        dependente.excluido = True
        dependente.save()
        msg = "Dependente excluído com sucesso!"
        tipo_msg = "Dependente excluído com sucesso!"
        return self.ListaDependentes(request, msg, tipo_msg)

    @classmethod
    def ListaDependentes(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        if request.GET or 'page' in request.GET:
            if request.GET.get('filtro'):
                dependente1 = DependenteModel.objects.filter(cpf__icontains=request.GET.get('filtro'), excluido=0)
                dependente2 = DependenteModel.objects.filter(nome__icontains=request.GET.get('filtro'), excluido=0)
                dependente3 = DependenteModel.objects.filter(email__icontains=request.GET.get('filtro'), excluido=0)
                dependentes = list(dependente1) + list(dependente2) + list(dependente3)
                dependentes = list(set(dependentes))
            else:
                dependentes = DependenteModel.objects.filter(excluido=False)
        else:
            dependentes = DependenteModel.objects.filter(excluido=False)

        dados, page_range, ultima = pagination(dependentes, request.GET.get('page'))
        context_dict['dados'] = dados
        context_dict['page_range'] = page_range
        context_dict['ultima'] = ultima
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        context_dict['filtro'] = request.GET.get('filtro')
        return render(request, self.template_lista, context_dict)
