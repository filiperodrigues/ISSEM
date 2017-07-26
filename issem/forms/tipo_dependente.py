#coding:utf-8
from django import forms
from issem.models.tipo_dependente import TipoDependenteModel


class TipoDependenteForm(forms.ModelForm):

    class Meta:
        model = TipoDependenteModel
        fields = '__all__'
