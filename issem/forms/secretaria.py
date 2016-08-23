# coding:utf-8
from django import forms
from issem.models import Secretaria


class SecretariaForm(forms.ModelForm):
    class Meta:
        model = Secretaria
        fields = ('nome',)
