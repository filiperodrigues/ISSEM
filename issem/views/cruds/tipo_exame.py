# coding:utf-8
from django.http import Http404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from issem.models import TipoExameModel
from issem.forms import TipoExameForm
from django.views.generic.base import View


class TipoExameView(View):
    template = 'cruds/tipo_exame.html'
    template_painel = 'paineis/funcionario_pagina.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    def get(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}
        if id:
            try:
                tipo_exame = TipoExameModel.objects.get(pk=id, excluido=False)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            except:
                raise Http404("Tipo de Exame não encontrado.")
            form = TipoExameForm(instance=tipo_exame)
        else:
            form = TipoExameForm()  # MODO CADASTRO: recebe o formulário vazio

        context_dict['form'] = form
        context_dict['id'] = id
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template, context_dict)

    def post(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        valido = False
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            try:
                tipo_exame = TipoExameModel.objects.get(pk=id, excluido=False)
            except:
                raise Http404("Tipo de Exame não encontrado.")
            form = TipoExameForm(instance=tipo_exame, data=request.POST)
            if form.is_valid():
                form.save()
                msg = 'Alterações realizadas com sucesso!'
                tipo_msg = 'green'
                valido = True
        else:  # CADASTRO NOVO
            id = None
            form = TipoExameForm(data=request.POST)
            if form.is_valid():
                form.save()
                msg = 'Tipo de dependente cadastrado com sucesso!'
                tipo_msg = 'green'
                form = TipoExameForm()
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
    def TipoExameDelete(self, request, id=None):
        context_dict = {}
        try:
            tipo_exame = TipoExameModel.objects.get(pk=id)
        except:
            raise Http404("Tipo de exame não encontrado.")
        tipo_exame.excluido = True
        tipo_exame.save()
        msg = 'Tipo de exame excluído com sucesso!'
        tipo_msg = 'green'
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template_painel, context_dict)
