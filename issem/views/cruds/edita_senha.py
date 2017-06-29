# coding:utf-8
from django.http import Http404
from issem.forms import PessoaPasswordForm
from django.views.generic.base import View
from issem.models import ServidorModel, SeguradoModel, DependenteModel
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.shortcuts import render


class EditaSenhaView(View):
    template = "cruds/edita_senha.html"

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    def get(self, request, id=None, id_group=None, msg=None, tipo_msg=None):
        context_dict = {}
        form = PessoaPasswordForm()
        try:
            group_user = Group.objects.get(pk=id_group).name
        except:
            raise Http404("Ocorreu algum erro, verifique e tente novamente.")
        if group_user == "Administrativo" or group_user == "Tecnico":
            try:
                nome = ServidorModel.objects.get(pk=id).nome
            except:
                raise Http404("Servidor não encontrado.")
        elif group_user == "Segurado":
            try:
                segurado = SeguradoModel.objects.get(pk=id)
                nome = segurado.nome
                if segurado.primeiro_login is True:
                    context_dict['msg'] = "Bem-vindo ao ISSEM. É necessário criar uma senha para ter acesso ao Sistema."
                    context_dict['msg_tipo_senha'] = "Defina sua senha"
                    context_dict['tipo_msg'] = "yellow"
            except:
                raise Http404("Segurado não encontrado.")
        else:
            try:
                nome = DependenteModel.objects.get(pk=id).nome
            except:
                raise Http404("Dependente não encontrado.")

        context_dict['form'] = form
        context_dict['id'] = id
        context_dict['nome'] = nome
        context_dict['id_group_user'] = id_group
        context_dict['group'] = group_user
        return render(request, self.template, context_dict)

    def post(self, request, id=None, id_group=None, msg=None, tipo_msg=None):
        context_dict = {}
        id = int(request.POST['id'])
        try:
            group_user = Group.objects.get(pk=id_group).name
        except:
            raise Http404("Ocorreu algum erro, verifique e tente novamente.")
        if group_user == "Administrativo" or group_user == "Tecnico":
            try:
                pessoa = ServidorModel.objects.get(pk=id)
            except:
                raise Http404("Servidor não encontrado.")
        elif group_user == "Segurado":
            try:
                pessoa = SeguradoModel.objects.get(pk=id)
            except:
                raise Http404("Segurado não encontrado.")
        else:
            try:
                pessoa = DependenteModel.objects.get(pk=id)
            except:
                raise Http404("Dependente não encontrado.")

        form = PessoaPasswordForm(instance=pessoa, data=request.POST)
        grupo = Group.objects.get(user=pessoa.id)
        if form.is_valid():
            form.save()
            if grupo.name == "Segurado":
                if pessoa.primeiro_login:
                    pessoa.primeiro_login = False
                    pessoa.save()
                    logout(request)
                    context_dict['msg'] = 'Sua nova senha foi cadastrada com sucesso! É necessário fazer login novamente para acessar o Sistema.'
                    context_dict['tipo_msg'] = 'green'
                    context_dict['login_required'] = True
                    return render(request, 'paineis/index.html', context_dict)
                else:
                    msg = 'Senha alterada com sucesso!'
                    tipo_msg = 'green'

            else:
                msg = 'Senha alterada com sucesso!'
                tipo_msg = 'green'
        else:
            print(form.errors)
            msg = 'Erros encontrados!'
            tipo_msg = 'red'

        context_dict['form'] = form
        context_dict['id'] = id
        context_dict['id_group_user'] = id_group
        context_dict['group'] = group_user
        context_dict['nome'] = pessoa
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template, context_dict)
