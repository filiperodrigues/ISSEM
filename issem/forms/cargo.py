#coding:utf-8
from django import forms
from issem.models import CargoModel


class CargoForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={}))

    class Meta:
        model = CargoModel
        fields = ('nome',)

