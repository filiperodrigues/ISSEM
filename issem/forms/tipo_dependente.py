#coding:utf-8
from django import forms
from issem.models import Tipo_Dependente


class Tipo_DependenteForm(forms.ModelForm):
    class Meta:
        model = Tipo_Dependente
        fields = ('nome',)
