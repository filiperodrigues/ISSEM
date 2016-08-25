#coding:utf-8
from django import forms
from issem.models.servidor import Servidor


class ServidorForm(forms.ModelForm):
    class Meta:
        model = Servidor
        fields = '__all__'
