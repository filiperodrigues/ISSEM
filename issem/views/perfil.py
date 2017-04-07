# coding:utf-8
from django.shortcuts import render
from issem.models import ServidorModel, SeguradoModel
from issem.forms import ServidorFormCad, SeguradoFormCad
from django.views.generic.base import View
from django.contrib.auth.models import Group


class PerfilView(View):
    template = 'perfil.html'

    def get(self, request, id=None):
        grupos = request.user.groups.all()
        group_user = None
        usuario = None
        if len(grupos) > 0:
            grupo_1 = str(grupos[0])

            if grupo_1 == "Técnico":
                group_user = False
                if id:  # EDIÇÃO
                    usuario = ServidorModel.objects.get(pk=id)
                    group_user = Group.objects.get(user=id).id

            elif grupo_1 == 'Segurado':
                group_user = False
                if id:  # EDIÇÃO
                    usuario = SeguradoModel.objects.get(pk=id)
                    group_user = Group.objects.get(user=id).id

            elif grupo_1 == 'Administrativo':
                group_user = False
                if id:  # EDIÇÃO
                    usuario = ServidorModel.objects.get(pk=id)
                    group_user = Group.objects.get(user=id).id

        return render(request, self.template, {'method': 'get', 'id': id, 'group_user': group_user, 'usuario': usuario})



# class EditaPerfilView(View):
