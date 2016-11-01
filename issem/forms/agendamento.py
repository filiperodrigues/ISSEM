# coding:utf-8
from django import forms
from issem.models.agendamento import AgendamentoModel
from issem.models.requerimento import RequerimentoModel
from issem.models.consulta_parametros import ConsultaParametrosModel
from issem.models.agendamento import AgendamentoModel
from django.shortcuts import HttpResponse
from datetime import date

class AgendamentoForm(forms.ModelForm):

    class Meta:
        model = AgendamentoModel
        fields = '__all__'

