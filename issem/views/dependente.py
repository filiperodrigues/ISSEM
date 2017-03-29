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
    template = 'dependente.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    @method_decorator(user_passes_test(group_test))

    def get(self, request, id=None, id_segurado=None):
        if id:
            dependente = DependenteModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = DependenteFormEdit(instance=dependente)
            group_user = Group.objects.get(user=id)
            id_group_user = group_user.id

        else:
            form = DependenteFormCad()  # MODO CADASTRO: recebe o formulário vazio
            id_group_user = ""

        return render(request, self.template, {'form': form, 'method': 'get', 'id': id, 'id_segurado': id_segurado, 'id_group_user' : id_group_user})

    def post(self, request, id_segurado=None):
        id_group_user = 0
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            dependente = DependenteModel.objects.get(pk=id)
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
            form = DependenteFormCad(data=request.POST)

            if form.is_valid():
                form.save()

                gp = Group.objects.get(name='Dependente')
                user = DependenteModel.objects.get(username=request.POST["username"])
                user.groups.add(gp)
                user.save()
                msg = 'Cadastro efetuado com sucesso!'
                tipo_msg = 'green'
                return render(request, 'blocos/mensagem_cadastro_concluido_dependente.html',
                              {'form': form, 'method': 'post', 'id': id, 'msg': msg, 'tipo_msg': tipo_msg,
                               'id_servidor': user.id})
            else:
                print(form.errors)
                msg = 'Erros encontrados!'
                tipo_msg = 'red'

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id, 'id_segurado': id_segurado, 'msg': msg, 'tipo_msg': tipo_msg, 'id_group_user' : id_group_user})

def ListaDependentes(request):
    dependentes = DependenteModel.objects.filter(excluido=False)
    dados, page_range, ultima = pagination(dependentes, request.GET.get('page'))
    return render(request, 'dependentes.html', {'dados': dados, 'page_range': page_range, 'ultima': ultima})


def DependenteDelete(request, id):
    dependente = DependenteModel.objects.get(pk=id)
    dependente.excluido = True
    dependente.save()
    return HttpResponseRedirect('/')
