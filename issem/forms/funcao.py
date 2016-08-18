#coding:utf-8
from django import forms
from issem.models import Funcao


class FuncaoForm(forms.ModelForm):
    class Meta:
        model = Funcao
        fields = ('nome',)
