# coding:utf-8
from django import forms

class FiltroAgendaForm(forms.ModelForm):
    data_inicio_periodo = forms.DateField(widget=forms.TextInput(attrs={'onfocus': 'limita_data_final'}))
    data_fim_periodo = forms.DateField(widget=forms.TextInput())
