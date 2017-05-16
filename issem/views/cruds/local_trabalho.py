 # coding:utf-8
from django.core import serializers
from django.http import Http404
from django.shortcuts import render, HttpResponse
from issem.models import EstadoModel
from issem.models import LocalTrabalhoModel
from issem.forms import LocalTrabalhoForm
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


class LocalTrabalhoView(View):
    template = 'cruds/local_trabalho.html'
    template_painel = 'paineis/funcionario_pagina.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}
        if id:  # EDIÇÃO
            try:
                local_trabalho = LocalTrabalhoModel.objects.get(pk=id, excluido=0)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            except:
                raise Http404("Local de Trabalho não encontrado.")
            form = LocalTrabalhoForm(instance=local_trabalho)
        else:  # CADASTRO NOVO
            form = LocalTrabalhoForm()  # MODO CADASTRO: recebe o formulário vazio

        context_dict['form'] = form
        context_dict['id'] = id
        context_dict['estados'] = EstadoModel.objects.all()
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
                local_trabalho = LocalTrabalhoModel.objects.get(pk=id, excluido=0)
            except:
                raise Http404("Loca de Trabalho não encontrado.")
            form = LocalTrabalhoForm(instance=local_trabalho, data=request.POST)
            if form.is_valid():
                form.save()
                msg = 'Alterações realizadas com sucesso!'
                tipo_msg = 'green'
                valido = True
        else:  # CADASTRO NOVO
            id = None
            form = LocalTrabalhoForm(data=request.POST)
            if form.is_valid():
                form.save()
                msg = 'Cargo cadastrado com sucesso!'
                tipo_msg = 'green'
                form = LocalTrabalhoForm()
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
    def LocalTrabalhoDelete(self, request, id=None):
        context_dict = {}
        try:
            local_trabalho = LocalTrabalhoModel.objects.get(pk=id)
        except:
            raise Http404("Local de Trabalho não encontrado.")
        local_trabalho.excluido = True
        local_trabalho.save()
        msg = 'Local de Trabalho excluído com sucesso!'
        tipo_msg = 'green'
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template_painel, context_dict)

    @classmethod
    @method_decorator(user_passes_test(group_test))
    def AtualizaLocalTrabalho(self, request):
        local_trabalhos = LocalTrabalhoModel.objects.filter(excluido=0)
        json = serializers.serialize("json", local_trabalhos)
        return HttpResponse(json)
