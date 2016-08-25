#coding:utf-8
from django import forms
from issem.models.segurado import Segurado


class SeguradoForm(forms.ModelForm):
    class Meta:
        model = Segurado
        fields = '__all__'
