# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import SeguradoModel
from issem.forms import PessoaPasswordForm, SeguradoFormEdit, SeguradoFormCad
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group
from issem.views.pagination import pagination


class SeguradoView(View):
    template = 'segurado.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id=None):
        if id:
            segurado = SeguradoModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = SeguradoFormEdit(instance=segurado)
        else:
            form = SeguradoFormCad()  # MODO CADASTRO: recebe o formulário vazio
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id})

    def post(self, request, id=None):
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            segurado = SeguradoModel.objects.get(pk=id)
            form = SeguradoFormEdit(instance=segurado, data=request.POST)

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
                msg = 'Cadastro efetuado com sucesso!'
                tipo_msg = 'green'
                return render(request, 'blocos/mensagem_cadastro_concluido_segurado.html',
                              {'form': form, 'method': 'post', 'id': id, 'msg': msg, 'tipo_msg': tipo_msg,
                               'id_segurado': user.id})
            else:
                print(form.errors)
                msg = 'Erros encontrados!'
                tipo_msg = 'red'

        return render(request, self.template,
                      {'form': form, 'method': 'post', 'id': id, 'msg': msg, 'tipo_msg': tipo_msg})


def SeguradoDelete(request, id):
    segurado = SeguradoModel.objects.get(pk=id)
    segurado.delete()
    msg = "Segurado excluído com sucesso!"
    tipo_msg = "green"
    return ListaSegurados(request, msg, tipo_msg)


def ListaSegurados(request, msg=None, tipo_msg=None):
    context_dict = {}
    segurados = SeguradoModel.objects.all()
    dados, page_range, ultima = pagination(segurados, request.GET.get('page'))
    context_dict['dados'] = dados
    context_dict['page_range'] = page_range
    context_dict['ultima'] = ultima

    if msg:
        context_dict['msg'] = msg
    if tipo_msg:
        context_dict['tipo_msg'] = tipo_msg

    return render(request, 'segurados.html', context_dict)


class EditaSenha(View):
    template = "edita_senha.html"

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id=None):
        form = PessoaPasswordForm()
        nome = SeguradoModel.objects.get(pk=id).nome
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id, 'nome': nome})

    def post(self, request, id=None):
        id = int(request.POST['id'])
        segurado = SeguradoModel.objects.get(pk=id)
        form = PessoaPasswordForm(instance=segurado, data=request.POST)

        if form.is_valid():
            form.save()
            msg = 'Senha alterada com sucesso!'
            tipo_msg = 'green'
        else:
            print(form.errors)
            msg = 'Erros encontrados!'
            tipo_msg = 'red'

        nome = SeguradoModel.objects.get(pk=id).nome
        return render(request, self.template,
                      {'form': form, 'method': 'post', 'id': id, 'msg': msg, 'tipo_msg': tipo_msg, 'nome': nome})
