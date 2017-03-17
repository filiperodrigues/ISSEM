# coding:utf-8
from django import forms


class FiltroAgendaForm(forms.Form):
    data_inicio_periodo = forms.DateField(widget=forms.DateInput(attrs={'onfocus': 'limita_data_final', 'type' : 'date'}))
    data_fim_periodo = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
