#coding:utf-8
from django import forms
from issem.models import ConsultasParametrosModel

class ConsultasParametrosForm(forms.ModelForm):
    tempo_consulta = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'class': 'minuto'}))
    tempo_espera = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'class': 'minuto'}))
    inicio_atendimento = forms.CharField(widget=forms.TextInput(attrs={'class': 'hora'}))
    class Meta:
        model = ConsultasParametrosModel
        fields = '__all__'
