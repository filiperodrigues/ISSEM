# coding:utf-8
from django import forms
from issem.models import SecretariaModel


class SecretariaForm(forms.ModelForm):
    class Meta:
        model = SecretariaModel
        fields = ('nome',)
