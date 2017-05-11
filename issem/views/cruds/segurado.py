# coding:utf-8
from django.shortcuts import render
from issem.models import SeguradoModel, RequerimentoModel
from issem.forms import PessoaPasswordForm, SeguradoFormEdit, SeguradoFormCad
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group
from issem.views.pagination import pagination


class SeguradoView(View):
    template = 'cruds/segurado.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo') or user.groups.filter(name='Segurado')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id=None):
        if id:
            segurado = SeguradoModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = SeguradoFormEdit(instance=segurado)
            group_user = Group.objects.get(user=id)
            id_group_user = group_user.id
        else:
            form = SeguradoFormCad()  # MODO CADASTRO: recebe o formulário vazio
            id_group_user = ""

        return render(request, self.template, {'form': form, 'id': id, 'id_group_user': id_group_user})

    def post(self, request, id=None):
        id_group_user = 0
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            segurado = SeguradoModel.objects.get(pk=id)
            form = SeguradoFormEdit(instance=segurado, data=request.POST)
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
            form = SeguradoFormCad(data=request.POST)

            if form.is_valid():
                form.save()

                gp = Group.objects.get(name='Segurado')
                user = SeguradoModel.objects.get(username=request.POST["username"])
                user.groups.add(gp)
                user.save()
                msg = "Cadastro efetuado com sucesso!"
                tipo_msg = 'green'
                form = SeguradoFormCad()
                return render(request, self.template, {'form': form, 'msg': msg, 'tipo_msg': tipo_msg, 'id_segurado': user.id, 'nome': user.nome})
            else:
                print(form.errors)
                msg = 'Erros encontrados!'
                tipo_msg = 'red'

        return render(request, self.template,
                      {'form': form, 'method': 'post', 'id': id, 'msg': msg, 'tipo_msg': tipo_msg,
                       'id_group_user': id_group_user})


def SeguradoDelete(request, id):
    segurado = SeguradoModel.objects.get(pk=id)
    segurado.excluido = True
    segurado.save()
    msg = "Segurado excluído com sucesso!"
    tipo_msg = "green"
    return ListaSegurados(request, msg, tipo_msg)


def ListaSegurados(request, msg=None, tipo_msg=None):
    if request.GET or 'page' in request.GET:
        if request.GET.get('filtro'):
            segurado1 = SeguradoModel.objects.filter(cpf__contains=request.GET.get('filtro'), excluido=0)
            segurado2 = SeguradoModel.objects.filter(nome__contains=request.GET.get('filtro'), excluido=0)
            segurado3 = SeguradoModel.objects.filter(email__contains=request.GET.get('filtro'), excluido=0)
            segurados = list(segurado1) + list(segurado2) + list(segurado3)
            segurados = list(set(segurados))
        else:
            segurados = SeguradoModel.objects.filter(excluido=False)
    else:
        segurados = SeguradoModel.objects.filter(excluido=False)

    dados, page_range, ultima = pagination(segurados, request.GET.get('page'))
    return render(request, 'listas/segurados.html',
                  {'dados': dados, 'page_range': page_range, 'ultima': ultima, 'msg': msg, 'tipo_msg': tipo_msg,
                   'filtro': request.GET.get('filtro')})

def ListaRequerimentosSegurado(request, id=None):
    context_dict = {}
    requerimentos = RequerimentoModel.objects.filter(segurado=id)
    print(requerimentos)
    dados, page_range, ultima = pagination(requerimentos, request.GET.get('page'))
    context_dict['dados'] = dados
    context_dict['page_range'] = page_range
    context_dict['ultima'] = ultima
    return render(request, 'listas/requerimentos_segurado.html', context_dict)
