# coding:utf-8
from django.http import Http404
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from issem.models import TipoDependenteModel
from issem.forms import TipoDependenteForm
from django.views.generic.base import View


class TipoDependenteView(View):
    template = 'cruds/tipo_dependente.html'
    template_painel = 'paineis/funcionario_pagina.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    def get(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}
        if id:
            try:
                tipo_dependente = TipoDependenteModel.objects.get(pk=id, excluido=0)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            except:
                raise Http404("Tipo de Dependente não encontrado.")

            form = TipoDependenteForm(instance=tipo_dependente)
        else:
            form = TipoDependenteForm()  # MODO CADASTRO: recebe o formulário vazio

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
                tipo_dependente = TipoDependenteModel.objects.get(pk=id, excluido=0)
            except:
                raise Http404("Tipo de dependente não encontrado.")
            form = TipoDependenteForm(instance=tipo_dependente, data=request.POST)
            if form.is_valid():
                form.save()
                msg = 'Alterações realizadas com sucesso!'
                tipo_msg = 'green'
                valido = True
        else:  # CADASTRO NOVO
            id = None
            form = TipoDependenteForm(data=request.POST)
            if form.is_valid():
                form.save()
                msg = 'Tipo de dependente cadastrado com sucesso!'
                tipo_msg = 'green'
                form = TipoDependenteForm()
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
    def TipoDependenteDelete(self, request, id=None):
        context_dict = {}
        try:
            cargo = TipoDependenteModel.objects.get(pk=id)
        except:
            raise Http404("Tipo de dependente não encontrado.")
        cargo.excluido = True
        cargo.save()
        msg = 'Tipo de dependente excluído com sucesso!'
        tipo_msg = 'green'
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template_painel, context_dict)
