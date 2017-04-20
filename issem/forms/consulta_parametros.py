# coding: utf-8
from django import forms
from issem.models import ParametrosConfiguracaoModel


class ConsultaParametrosForm(forms.ModelForm):

    class Meta:
        model = ParametrosConfiguracaoModel
        fields = '__all__'
