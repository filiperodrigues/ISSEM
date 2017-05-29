# coding:utf-8
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from issem.models import BeneficioModel, AgendamentoModel
from datetime import date, timedelta
from django.db.models import Q


class PaginaFuncionarioView(View):
    template = 'paineis/funcionario_pagina.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        hoje_mais_um_dia = date.today() + timedelta(days=1)
        hoje_mais_dois_dias = date.today() + timedelta(days=2)
        context_dict['proximos_agendamentos'] = AgendamentoModel.objects.filter(
            Q(data_pericia=hoje_mais_um_dia) | Q(data_pericia=hoje_mais_dois_dias)).order_by('data_pericia')
        context_dict['beneficios'] = BeneficioModel.objects.filter(excluido=False)
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template, context_dict)


class PaginaMedicoView(View):
    template = 'paineis/medico_pagina.html'

    def group_test(user):
        return user.groups.filter(name='Tecnico')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template, context_dict)


class PaginaSeguradoView(View):
    template = 'paineis/segurado_pagina.html'

    def group_test(user):
        return user.groups.filter(name='Segurado')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        context_dict['beneficios'] = BeneficioModel.objects.all()
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template, context_dict)
