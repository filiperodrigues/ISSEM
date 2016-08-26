#coding:utf-8
from django import forms
from issem.models import BeneficioModel


class BeneficioForm(forms.ModelForm):
    class Meta:
        model = BeneficioModel
        fields = ('concessao', 'data_inicial', 'data_final', 'data_retorno', 'data_pericia', 'descricao', 'numero_portaria', 'data_portaria', 'salario_maximo', 'observacao', 'carencia')
