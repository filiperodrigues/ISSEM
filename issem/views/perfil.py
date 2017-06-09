# coding:utf-8
from django.http import Http404
from django.shortcuts import render
from issem.models import ServidorModel, SeguradoModel, DependenteModel
from django.views.generic.base import View
from django.contrib.auth.models import Group, User


class PerfilView(View):
    template = 'estatico/perfil.html'

    def get(self, request, id=None):
        dependente = None
        segurado = None
        context_dict = {}

        try:
            usuario = User.objects.get(pk=id)
        except:
            raise Http404("Usuário não encontrado.")
        try:
            grupo = usuario.groups.get()
        except:
            raise Http404("Grupo do usuário não encontrado.")

        if str(grupo) == "Administrativo" or str(grupo) == "Tecnico":
            administrador = ServidorModel.objects.get(id=request.user.id)
            context_dict['administrador'] = administrador.administrador
            grupo = False
            try:
                usuario = ServidorModel.objects.get(pk=id)
            except:
                raise Http404("Usuário não encontrado.")

        elif str(grupo) == 'Segurado':
            grupo = False
            try:
                usuario = SeguradoModel.objects.get(pk=id)
            except:
                raise Http404("Segurado não encontrado.")
            dependente = usuario.dependente.filter(excluido=False)

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

        usuario_logado = User.objects.get(pk=request.user.id)
        context_dict['id'] = id
        context_dict['group_user'] = grupo
        context_dict['usuario'] = usuario
        context_dict['segurado'] = segurado
        context_dict['dependente'] = dependente
        context_dict['usuario_logado'] = usuario_logado.id
        return render(request, self.template, context_dict)
