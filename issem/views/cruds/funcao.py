# coding:utf-8
from django.http import Http404
from django.shortcuts import render
from issem.models import FuncaoModel
from issem.forms import FuncaoForm
from django.views.generic.base import View


class FuncaoView(View):
    template = 'cruds/funcao.html'
    template_painel = 'paineis/funcionario_pagina.html'

    def get(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}
        if id:
            try:
                funcao = FuncaoModel.objects.get(pk=id, excluido=False)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            except:
                raise Http404("Função não encontrada.")
            form = FuncaoForm(instance=funcao)
        else:
            form = FuncaoForm()  # MODO CADASTRO: recebe o formulário vazio

        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        context_dict['form'] = form
        context_dict['id'] = id
        return render(request, self.template, context_dict)

    def post(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        valido = False
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            try:
                funcao = FuncaoModel.objects.get(pk=id, excluido=False)
            except:
                raise Http404("Função não encontrada.")
            form = FuncaoForm(instance=funcao, data=request.POST)
            if form.is_valid():
                form.save()
                msg = 'Alterações realizadas com sucesso!'
                tipo_msg = 'green'
                valido = True
        else:  # CADASTRO NOVO
            id = None
            form = FuncaoForm(data=request.POST)
            if form.is_valid():
                form.save()
                msg = 'Função cadastrada com sucesso!'
                tipo_msg = 'green'
                form = FuncaoForm()
                valido = True

        if not valido:
            print(form.errors)
            msg = 'Erros encontrados!'
            tipo_msg = 'red'

        context_dict['id'] = id
        context_dict['form'] = form
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template, context_dict)

    @classmethod
    def FuncaoDelete(self, request, id=None):
        context_dict = {}
        try:
            funcao = FuncaoModel.objects.get(pk=id)
        except:
            raise Http404("Função não encontrada.")
        funcao.excluido = True
        funcao.save()
        msg = 'Exclusão efetuada com sucesso!'
        tipo_msg = 'green'
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template_painel, context_dict)
