# coding:utf-8
from django.shortcuts import render
from issem.models import ServidorModel, SeguradoModel, DependenteModel
from django.views.generic.base import View
from django.contrib.auth.models import Group, User


class PerfilView(View):
    template = 'perfil/perfil.html'

    def get(self, request, id=None):
        usuario = User.objects.get(pk=id)
        grupo = usuario.groups.get()

        if grupo != "":
            if str(grupo) == "Administrativo" or str(grupo) == "Tecnico":
                grupo = False
                if id:  # EDIÇÃO
                    usuario = ServidorModel.objects.get(pk=id)
                    grupo = Group.objects.get(user=id).id

            elif str(grupo) == 'Segurado':
                grupo = False
                if id:  # EDIÇÃO
                    usuario = SeguradoModel.objects.get(pk=id)
                    grupo = Group.objects.get(user=id).id

            elif str(grupo) == 'Dependente':
                grupo = False
                if id:  # EDIÇÃO
                    usuario = DependenteModel.objects.get(pk=id)
                    grupo = Group.objects.get(user=id).id

        return render(request, self.template, {'method': 'get', 'id': id, 'group_user': grupo, 'usuario': usuario})
