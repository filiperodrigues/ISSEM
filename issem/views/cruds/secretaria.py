# coding:utf-8
from django.http import Http404
from django.shortcuts import render, HttpResponse
from issem.models import SecretariaModel
from issem.forms import SecretariaForm
from django.views.generic.base import View
from django.core import serializers
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


class SecretariaView(View):
    template = 'cruds/secretaria.html'
    template_painel = 'paineis/funcionario_pagina.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}
        if id:
            try:
                secretaria = SecretariaModel.objects.get(pk=id, excluido=False)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            except:
                raise Http404("Secretaria não encontrada.")
            form = SecretariaForm(instance=secretaria)
        else:
            form = SecretariaForm()  # MODO CADASTRO: recebe o formulário vazio

        context_dict['form'] = form
        context_dict['id'] = id
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template, context_dict)

    @method_decorator(user_passes_test(group_test))
    def post(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        valido = False

        #TODO: PARA CADASTRO DENTRO DO MODAL
        if 'sec' in request.POST:
            nome = request.POST['sec']
            nome_sec = SecretariaModel(nome=nome)
            nome_sec.save()
            nome_sec = SecretariaModel.objects.filter(excluido=False)
            json = serializers.serialize("json", nome_sec)
            return HttpResponse(json)

        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            try:
                secretaria = SecretariaModel.objects.get(pk=id, excluido=False)
            except:
                raise Http404("Secretaria não encontrada.")
            form = SecretariaForm(instance=secretaria, data=request.POST)
            if form.is_valid():
                form.save()
                msg = 'Alterações realizadas com sucesso!'
                tipo_msg = 'green'
                valido = True
        else:  # CADASTRO NOVO
            id = None
            form = SecretariaForm(data=request.POST)
            if form.is_valid():
                form.save()
                msg = 'Secretaria cadastrada com sucesso!'
                tipo_msg = 'green'
                form = SecretariaForm()
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
    def SecretariaDelete(self, request, id=None):
        context_dict = {}
        try:
            secretaria = SecretariaModel.objects.get(pk=id)
        except:
            raise Http404("Secretaria não encontrada.")
        secretaria.excluido = True
        secretaria.save()
        msg = 'Secretaria excluída com sucesso!'
        tipo_msg = 'green'
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template_painel, context_dict)

    @classmethod
    @method_decorator(user_passes_test(group_test))
    def AtualizaSecretaria(self, request):

        secretarias = SecretariaModel.objects.filter(excluido=False)
        json = serializers.serialize("json", secretarias)
        return HttpResponse(json)
