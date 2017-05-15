# coding:utf-8
from django.http import Http404
from django.shortcuts import render,HttpResponse
from issem.models import CargoModel
from issem.forms import CargoForm
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.core import serializers



class CargoView(View):
    template = 'cruds/cargo.html'
    template_painel = 'paineis/funcionario_pagina.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}
        if id:  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            try:
                cargo = CargoModel.objects.get(pk=id, excluido=0)
            except:
                raise Http404("Cargo não encontrado.")
            form = CargoForm(instance=cargo)
        else:  # MODO CADASTRO: recebe o formulário vazio
            form = CargoForm()

        context_dict['form'] = form
        context_dict['id'] = id
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template, context_dict)

    @method_decorator(user_passes_test(group_test))
    def post(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        valido = False
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            try:
                cargo = CargoModel.objects.get(pk=id, excluido=0)
            except:
                raise Http404("Cargo não encontrado.")
            form = CargoForm(instance=cargo, data=request.POST)
            if form.is_valid():
                form.save()
                msg = 'Alterações realizadas com sucesso!'
                tipo_msg = 'green'
                valido = True
        else:  # CADASTRO NOVO
            id = None
            form = CargoForm(data=request.POST)
            if form.is_valid():
                form.save()
                msg = 'Cargo cadastrado com sucesso!'
                tipo_msg = 'green'
                form = CargoForm()
                valido = True

        if not valido:
            print(form.errors)
            msg = 'Erros encontrados!'
            tipo_msg = 'red'

        context_dict['form'] = form
        context_dict['id'] = id
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template, context_dict)

    @classmethod
    @method_decorator(user_passes_test(group_test))
    def CargoDelete(self, request, id=None):
        context_dict = {}
        try:
            cargo = CargoModel.objects.get(pk=id)
        except:
            raise Http404("Cargo não encontrado.")
        cargo.excluido = True
        cargo.save()
        context_dict['msg'] = 'Cargo excluído com sucesso!'
        context_dict['tipo_msg'] = 'green'
        return render(request, self.template_painel, context_dict)

    @classmethod
    @method_decorator(user_passes_test(group_test))
    def AtualizaCargo(self,request):

        cargos = CargoModel.objects.filter(excluido=0)
        json = serializers.serialize("json", cargos)
        return HttpResponse(json)
