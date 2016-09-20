#coding:utf-8
from django import forms
from issem.models.segurado import SeguradoModel


class SeguradoForm(forms.ModelForm):

    class Meta:
        model = SeguradoModel
        fields = '__all__'
