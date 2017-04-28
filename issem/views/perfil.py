# coding:utf-8
from django.http import Http404
from django.shortcuts import render
from issem.models import ServidorModel, SeguradoModel, DependenteModel
from django.views.generic.base import View
from django.contrib.auth.models import Group, User


class PerfilView(View):
    template = 'perfil/perfil.html'

    def get(self, request, id=None):
        context_dict = {}
        segurado = None
        try:
            usuario = User.objects.get(pk=id)
        except:
            raise Http404("Usuário não encontrado.")
        try:
            grupo = usuario.groups.get()
        except:
            raise Http404("Grupo do usuário não encontrado.")

        if str(grupo) == "Administrativo" or str(grupo) == "Tecnico":
            grupo = False
            try:
                usuario = ServidorModel.objects.get(pk=id)
            except:
                raise Http404("Usuário não encontrado.")
        elif str(grupo) == 'Segurado':
            grupo = False
            usuario = SeguradoModel.objects.get(pk=id)
        elif str(grupo) == 'Dependente':
            grupo = False
            try:
                usuario = DependenteModel.objects.get(pk=id)
            except:
                raise Http404("Usuário não encontrado.")
            try:
                segurado = SeguradoModel.objects.get(dependente__id=id)
            except:
                segurado = None
        else:
            raise Http404("Grupo do usuário não encontrado.")

        context_dict['id'] = id
        context_dict['group_user'] = grupo
        context_dict['usuario'] = usuario
        context_dict['segurado'] = segurado
        return render(request, self.template, context_dict)
