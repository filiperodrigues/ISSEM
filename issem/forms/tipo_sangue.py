# coding:utf-8
from django import forms
from issem.models import TipoSangueModel


class TipoSangueForm(forms.ModelForm):
    class Meta:
        model = TipoSangueModel
        fields = ('nome',)
