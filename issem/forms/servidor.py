#coding:utf-8
from django import forms
from issem.models.servidor import ServidorModel


class ServidorForm(forms.ModelForm):
    class Meta:
        model = ServidorModel
        fields = '__all__'
