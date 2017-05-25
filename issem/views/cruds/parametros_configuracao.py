# coding:utf-8
from django.http import Http404
from django.shortcuts import render
from issem.models import ParametrosConfiguracaoModel
from issem.forms import ParametrosConfiguracaoForm
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


class ParametrosConfiguracaoView(View):
    template = 'cruds/parametros_configuracao.html'
    template_painel = 'paineis/funcionario_pagina.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        try:
            consulta_parametros = ParametrosConfiguracaoModel.objects.all().last()
        except:
            raise Http404("Parâmetros de Configuração não encontrados.")
        form = ParametrosConfiguracaoForm(instance=consulta_parametros)

        context_dict['form'] = form
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        context_dict['id'] = 1
        return render(request, self.template, context_dict)

    @method_decorator(user_passes_test(group_test))
    def post(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        try:
            consulta_parametros = ParametrosConfiguracaoModel.objects.all().last()
        except:
            raise Http404("Parâmetros de Configuração não encontrados.")
        form = ParametrosConfiguracaoForm(instance=consulta_parametros, data=request.POST)

        if form.is_valid():
            form.save()
            msg = 'Alterações realizadas com sucesso!'
            tipo_msg = 'green'
        else:
            print(form.errors)
            msg = 'Erros encontrados!'
            tipo_msg = 'red'

        context_dict['form'] = form
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        context_dict['id'] = 1
        return render(request, self.template, context_dict)
