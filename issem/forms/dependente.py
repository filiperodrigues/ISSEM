#coding:utf-8
from django import forms
from issem.models.dependente import Dependente


class DependenteForm(forms.ModelForm):
    class Meta:
        model = Dependente
        fields = '__all__'