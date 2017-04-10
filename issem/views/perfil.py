# coding:utf-8
from django.shortcuts import render
from issem.models import ServidorModel, SeguradoModel, DependenteModel
from django.views.generic.base import View
from django.contrib.auth.models import Group, User


class PerfilView(View):
    template = 'perfil.html'

    def get(self, request, id=None):
        usuario = User.objects.get(pk=id)
        group_user = usuario.groups.all()[0]

        if group_user != "":

            if str(group_user) == "Administrativo" or str(group_user) == "Tecnico":
                group_user = False
                if id:  # EDIÇÃO
                    usuario = ServidorModel.objects.get(pk=id)
                    group_user = Group.objects.get(user=id).id

            elif str(group_user) == 'Segurado':
                group_user = False
                if id:  # EDIÇÃO
                    usuario = SeguradoModel.objects.get(pk=id)
                    group_user = Group.objects.get(user=id).id

            elif str(group_user) == 'Dependente':
                group_user = False
                if id:  # EDIÇÃO
                    usuario = DependenteModel.objects.get(pk=id)
                    group_user = Group.objects.get(user=id).id

        return render(request, self.template, {'method': 'get', 'id': id, 'group_user': group_user, 'usuario': usuario})

# class EditaPerfil(View):
#     template = edita
