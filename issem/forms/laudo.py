# coding: utf-8
from django import forms
from issem.models import LaudoModel


class LaudoForm(forms.ModelForm):

    class Meta:
        model = LaudoModel
        fields = '__all__'
