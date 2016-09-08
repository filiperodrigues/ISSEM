#coding:utf-8
from django import forms
from issem.models.segurado import SeguradoModel

class SeguradoForm(forms.ModelForm):
    cpf = forms.CharField(max_length=11)
    class Meta:
        model = SeguradoModel
        fields = '__all__'

