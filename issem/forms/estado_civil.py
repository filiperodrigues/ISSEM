#coding:utf-8
from django import forms
from issem.models import EstadoCivilModel


class EstadoCivilForm(forms.ModelForm):
    class Meta:
        model = EstadoCivilModel
        fields = ('nome',)