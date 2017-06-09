# coding:utf-8
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from issem.variaveis_sistema import *
from issem.models import ServidorModel, SeguradoModel, DependenteModel


class Grupo(View):
    template = 'estatico/altera_grupo.html'
    index='paineis/funcionario_pagina.html'

    def group_test(user):
        return user.groups.filter(name=ADMINISTRATIVO)

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id=None):
        context_dict = {}
        usuario = User.objects.get(id=id)
        grupo = usuario.groups.all()[0]
        grupos = Group.objects.all()
        if grupo.name == ADMINISTRATIVO:
            nome = ServidorModel.objects.get(id=id).nome
        elif grupo.name == TECNICO:
            nome = ServidorModel.objects.get(id=id).nome
        elif grupo.name == SEGURADO:
            nome = SeguradoModel.objects.get(id=id).nome
        else:
            nome = DependenteModel.objects.get(id=id).nome
        context_dict['grupos'] = grupos
        context_dict['nome'] = nome
        context_dict['grupo'] = grupo
        context_dict['id'] = usuario.id

        return render(request, self.template, context_dict )

    @method_decorator(user_passes_test(group_test))
    def post(self, request, id=None):
        print ("oiioiioioio")
        usuario = User.objects.get(id=id)
        grupo_antigo = usuario.groups.all()
        novo_grupo = request.POST.getlist('grupos')
        try:
            if request.POST.get('opcao') == '1':
                for i in grupo_antigo:
                    grupo=Group.objects.get(pk=i.id)
                    usuario.groups.remove(grupo)

            for id in novo_grupo:
                grupo = Group.objects.get(pk=id)
                usuario.groups.add(grupo)

        except:
            pass
        context_dict = {}
        usuario = User.objects.get(id=id)
        context_dict['id'] = usuario.id

        return render(request, self.index, context_dict )
