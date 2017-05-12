# coding:utf-8
from django.http import Http404
from django.shortcuts import render
from issem.models import TipoLaudoModel
from issem.forms import TipoLaudoForm
from django.views.generic.base import View
from issem.views.pagination import pagination
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test


class TipoLaudoView(View):
    template = 'cruds/tipo_laudo.html'
    template_painel = 'paineis/funcionario_pagina.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    def get(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}
        if id:
            try:
                tipo_Laudo = TipoLaudoModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            except:
                raise Http404("Tipo de Laudo não encontrado")
            form = TipoLaudoForm(instance=tipo_Laudo)
        else:
            form = TipoLaudoForm()  # MODO CADASTRO: recebe o formulário vazio

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
                tipo_Laudo = TipoLaudoModel.objects.get(pk=id)
            except:
                raise Http404("Tipo de laudo não encontrado.")
            form = TipoLaudoForm(instance=tipo_Laudo, data=request.POST)
            if form.is_valid():
                form.save()
                msg = 'Alterações realizadas com sucesso!'
                tipo_msg = 'green'
                valido = True
        else:  # CADASTRO NOVO
            id = None
            form = TipoLaudoForm(data=request.POST)
            if form.is_valid():
                form.save()
                msg = 'Tipo de laudo cadastrado com sucesso!'
                tipo_msg = 'green'
                form = TipoLaudoForm()
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
    def TipoLaudoDelete(self, request, id=None):
        context_dict = {}
        try:
            cargo = TipoLaudoModel.objects.get(pk=id)
        except:
            raise Http404("Tipo de laudo não encontrado.")
        cargo.delete()
        msg = 'Tipo de laudo excluído com sucesso!'
        tipo_msg = 'green'
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template_painel, context_dict)

    @classmethod
    def ListaTiposLaudos(self, request, msg=None, tipo_msg=None):
        if request.GET or 'page' in request.GET:
            if request.GET.get('filtro'):
                tipos_laudos = TipoLaudoModel.objects.filter(nome__icontains=request.GET.get('filtro'), excluido=0)
            else:
                tipos_laudos = TipoLaudoModel.objects.filter(excluido=False)
        else:
            tipos_laudos = TipoLaudoModel.objects.filter(excluido=False)

        dados, page_range, ultima = pagination(tipos_laudos, request.GET.get('page'))
        return render(request, 'listas/tipos_laudo.html',
                      {'dados': dados, 'page_range': page_range, 'ultima': ultima, 'msg': msg, 'tipo_msg': tipo_msg,
                       'filtro': request.GET.get('filtro')})

    @classmethod
    def TipoLaudoDelete(self, request, id):
        try:
            tipo_Laudo = TipoLaudoModel.objects.get(pk=id)
        except:
            raise Http404("Tipos de laudo não encontrado.")
        tipo_Laudo.excluido = True
        tipo_Laudo.save()
        msg = "Tipo de Laudo excluído com sucesso!"
        tipo_msg = 'green'
        return self.ListaTiposLaudos(request, msg, tipo_msg)