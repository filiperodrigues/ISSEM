#coding:utf-8
from django import forms
from issem.models import Tipo_Exame


class Tipo_ExameForm(forms.ModelForm):
    class Meta:
        model = Tipo_Exame
        fields = ('nome', 'observacao',)