# coding:utf-8
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from issem.models import BeneficioModel, AgendamentoModel, RequerimentoModel
from datetime import date, timedelta
from django.db.models import Q
from django.contrib.auth.models import User


class PaginaFuncionarioView(View):
    template = 'paineis/funcionario_pagina.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        amanha = date.today() + timedelta(days=1)
        depois_de_amanha = date.today() + timedelta(days=2)
        agendamentos = AgendamentoModel.objects.filter(
            Q(data_pericia=date.today()) |
            Q(data_pericia=amanha) |
            Q(data_pericia=depois_de_amanha)).order_by('data_pericia')[:10]
        num_agendamentos = len(agendamentos)
        context_dict['agendamentos'] = agendamentos
        context_dict['num_agendamentos'] = num_agendamentos
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
        if RequerimentoModel.objects.filter(segurado=User.objects.get(pk=request.user.id), possui_agendamento=False):
            requerimento = RequerimentoModel.objects.get(segurado=User.objects.get(pk=request.user.id), possui_agendamento=False)
            context_dict['possui_requerimento_aberto'] = True
            context_dict['id_requerimento_sem_agendamento'] = requerimento.id
        return render(request, self.template, context_dict)
