# coding:utf-8
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from issem.models import BeneficioModel, AgendamentoModel
from datetime import date, timedelta
from django.db.models import Q


class PaginaFuncionarioView(View):

    template = 'funcionario_pagina.html'

    def group_test(user):
        return user.groups.filter(name='Servidor')

    @method_decorator(user_passes_test(group_test))

    def get(self, request):
        context_dict = {}
        context_dict['beneficios'] = BeneficioModel.objects.all()
        hoje_mais_um_dia = date.today() + timedelta(days=1)
        hoje_mais_dois_dias = date.today() + timedelta(days=2)
        context_dict['proximos_agendamentos'] = AgendamentoModel.objects.filter(Q(data_pericia=hoje_mais_um_dia) | Q(data_pericia=hoje_mais_dois_dias)).order_by('data_pericia')
        return render(request, self.template, context_dict)