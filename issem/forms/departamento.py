#coding:utf-8
from django import forms
from issem.models import DepartamentoModel


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = DepartamentoModel
        fields = ('nome',)
