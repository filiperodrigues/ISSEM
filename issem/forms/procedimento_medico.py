#coding:utf-8
from django import forms
from issem.models.procedimento_medico import ProcedimentoMedicoModel


class ProcedimentoMedicoForm(forms.ModelForm):

    class Meta:
        model = ProcedimentoMedicoModel
        fields = '__all__'
