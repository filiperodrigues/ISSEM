#coding:utf-8
from django import forms
from issem.models.funcao import FuncaoModel


class FuncaoForm(forms.ModelForm):

    class Meta:
        model = FuncaoModel
        fields = '__all__'
