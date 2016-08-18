# coding:utf-8
from django import forms
from issem.models import Tipo_Sangue


class Tipo_SangueForm(forms.ModelForm):
    class Meta:
        model = Tipo_Sangue
        fields = ('nome',)
