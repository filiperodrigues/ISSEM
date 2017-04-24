# coding:utf-8
from issem.forms import ServidorFormCad, PessoaPasswordForm, ServidorFormEdit
from django.views.generic.base import View
from django.utils.decorators import method_decorator
from issem.models import ServidorModel, SeguradoModel, DependenteModel
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import Group


class EditaSenha(View):
    template = "cruds/edita_senha.html"

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    def get(self, request, id=None, id_group=None):
        form = PessoaPasswordForm()
        group_user = Group.objects.get(pk=id_group).name
        if group_user == "Administrativo" or group_user == "Tecnico":
            nome = ServidorModel.objects.get(pk=id).nome
        elif group_user == "Segurado":
            nome = SeguradoModel.objects.get(pk=id).nome
        else:
            nome = DependenteModel.objects.get(pk=id).nome
        return render(request, self.template,
                      {'form': form, 'method': 'get', 'id': id, 'nome': nome, 'id_group_user': id_group, 'group': group_user})

    def post(self, request, id=None, id_group=None):
        id = int(request.POST['id'])
        group_user = Group.objects.get(pk=id_group).name
        if group_user == "Administrativo" or group_user == "Tecnico":
            pessoa = ServidorModel.objects.get(pk=id)
        elif group_user == "Segurado":
            pessoa = SeguradoModel.objects.get(pk=id)
        else:
            pessoa = DependenteModel.objects.get(pk=id)

        form = PessoaPasswordForm(instance=pessoa, data=request.POST)
        if form.is_valid():
            form.save()
            msg = 'Senha alterada com sucesso!'
            tipo_msg = 'green'
        else:
            print(form.errors)
            msg = 'Erros encontrados!'
            tipo_msg = 'red'

        return render(request, self.template,
                      {'form': form, 'method': 'post', 'id': id, 'msg': msg, 'tipo_msg': tipo_msg, 'nome': pessoa,
                       'id_group_user': id_group, 'group': group_user})
