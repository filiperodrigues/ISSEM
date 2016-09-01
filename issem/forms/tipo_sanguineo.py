# coding:utf-8
from django import forms
from issem.models import TipoSanguineoModel


class TipoSanguineoForm(forms.ModelForm):
    class Meta:
        model = TipoSanguineoModel
        fields = ('nome',)
