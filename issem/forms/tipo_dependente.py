#coding:utf-8
from django import forms
from issem.models import TipoDependenteModel


class TipoDependenteForm(forms.ModelForm):

    class Meta:
        model = TipoDependenteModel
        fields = ('descricao',)
