#coding:utf-8
from django import forms
from issem.models import Procedimento_Medico


class Procedimento_MedicoForm(forms.ModelForm):
    class Meta:
        model = Procedimento_Medico
        fields = ('codigo', 'descricao', 'porte', 'custo_operacao')
