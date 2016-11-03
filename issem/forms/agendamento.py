# coding:utf-8
from django import forms
from issem.models.agendamento import AgendamentoModel
from issem.models.requerimento import RequerimentoModel
from issem.models.consulta_parametros import ConsultaParametrosModel
from issem.models.agendamento import AgendamentoModel
from django.shortcuts import HttpResponse
from datetime import date

time_widget = forms.widgets.TimeInput(attrs={'class': 'time-pick'})
class AgendamentoForm(forms.ModelForm):
    hora_pericia = forms.TimeField(widget=time_widget, help_text='ex: 10:30AM')

    class Meta:
        model = AgendamentoModel
        fields = '__all__'

