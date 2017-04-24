# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import DependenteModel, SeguradoModel
from issem.forms import DependenteFormCad, DependenteFormEdit
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group
from issem.views.pagination import pagination


class DependenteView(View):
    template = 'cruds/dependente.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id=None, id_segurado=None):
        segurado = None
        id_group_user = None
        msg = None
        tipo_msg = None
        if not id and id_segurado:
            segurado = SeguradoModel.objects.get(pk=id_segurado)
            form = DependenteFormCad()  # MODO CADASTRO: recebe o formulário vazio, para um segurado específico
        elif id and not id_segurado:
            dependente = DependenteModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            try:
                segurado = SeguradoModel.objects.get(dependente__id=id)
            except:
                segurado = None
                msg = 'Dependente não está associado à nenhum segurado!'
                tipo_msg = 'red'
            form = DependenteFormEdit(instance=dependente)
            id_group_user = Group.objects.get(user=id).id
        else:
            form = DependenteFormCad()  # MODO CADASTRO: recebe o formulário vazio
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id, 'id_segurado': id_segurado,
                                               'id_group_user': id_group_user, 'segurado': segurado, 'msg': msg, 'tipo_msg': tipo_msg})

    def post(self, request, id_segurado=None):
        id_group_user = None
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            dependente = DependenteModel.objects.get(pk=id)
            segurado = SeguradoModel.objects.get(dependente=dependente)
            form = DependenteFormEdit(instance=dependente, data=request.POST)
            group_user = Group.objects.get(user=id)
            id_group_user = group_user.id

            if form.is_valid():
                form.save()
                msg = 'Alterações realizadas com sucesso!'
                tipo_msg = 'green'
            else:
                print(form.errors)
                msg = 'Erros encontrados!'
                tipo_msg = 'red'

        else:  # CADASTRO NOVO
            id = None
            id_segurado = request.POST['id_segurado']
            segurado = SeguradoModel.objects.get(pk=id_segurado)
            form = DependenteFormCad(data=request.POST)

            if form.is_valid():
                form.save()

                gp = Group.objects.get(name='Dependente')
                user = DependenteModel.objects.get(username=request.POST["username"])
                user.groups.add(gp)
                user.is_active = False
                user.save()
                segurado.dependente.add(user)
                segurado.save()
                msg = 'Cadastro efetuado com sucessooooo!'
                tipo_msg = 'green'
                form = DependenteFormCad()
                return render(request, self.template,
                              {'form': form, 'msg': msg, 'tipo_msg': tipo_msg, 'id_segurado': id_segurado, 'segurado': segurado})
            else:
                print(form.errors)
                msg = 'Erros encontrados!'
                tipo_msg = 'red'

        return render(request, self.template,
                      {'form': form, 'method': 'post', 'id': id, 'segurado': segurado, 'msg': msg,
                       'tipo_msg': tipo_msg, 'id_group_user': id_group_user})


def DependenteDelete(request, id):
    dependente = DependenteModel.objects.get(pk=id)
    dependente.excluido = True
    dependente.save()
    return ListaDependentes(request, msg="Dependente excluído com sucesso!", tipo_msg="green")


def ListaDependentes(request, msg=None, tipo_msg=None):
    dependentes = DependenteModel.objects.filter(excluido=False)
    dados, page_range, ultima = pagination(dependentes, request.GET.get('page'))
    return render(request, 'listas/dependentes.html',
                  {'dados': dados, 'page_range': page_range, 'ultima': ultima, 'msg': msg, 'tipo_msg': tipo_msg})
