#coding:utf-8
from django import forms
from issem.models import Departamento


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ('nome',)
