# coding:utf-8
from django.shortcuts import render
from issem.models import ServidorModel, SeguradoModel, DependenteModel
from django.views.generic.base import View
from django.contrib.auth.models import Group, User


class PerfilView(View):
    template = 'perfil.html'

    def get(self, request, id=None):
        grupo = User.objects.get(id=id)
        group_user = None
        usuario = None
        print(grupo)
        if grupo != "":
            # grupo_1 = str(grupos[0])

            if str(grupo) == "servidor" or str(grupo) == "medico":
                group_user = False
                if id:  # EDIÇÃO
                    usuario = ServidorModel.objects.get(pk=id)
                    group_user = Group.objects.get(user=id).id

            elif str(grupo) == 'segurado':
                group_user = False
                if id:  # EDIÇÃO
                    usuario = SeguradoModel.objects.get(pk=id)
                    group_user = Group.objects.get(user=id).id

            elif str(grupo) == 'dependente':
                group_user = False
                if id:  # EDIÇÃO
                    usuario = DependenteModel.objects.get(pk=id)
                    group_user = Group.objects.get(user=id).id

        return render(request, self.template, {'method': 'get', 'id': id, 'group_user': group_user, 'usuario': usuario})

# class EditaPerfil(View):
#     template = edita
