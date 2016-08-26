#coding:utf-8
from django import forms
from issem.models.dependente import DependenteModel


class DependenteForm(forms.ModelForm):
    class Meta:
        model = DependenteModel
        fields = '__all__'