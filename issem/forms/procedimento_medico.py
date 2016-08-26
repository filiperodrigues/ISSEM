#coding:utf-8
from django import forms
from issem.models import ProcedimentoMedicoModel

class ProcedimentoMedicoForm(forms.ModelForm):
    class Meta:
        model = ProcedimentoMedicoModel
        fields = ('codigo', 'descricao', 'porte', 'custo_operacao')
