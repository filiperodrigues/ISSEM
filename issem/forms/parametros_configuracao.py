# coding: utf-8
from django import forms
from issem.models.parametros_configuracao import ParametrosConfiguracaoModel


class ParametrosConfiguracaoForm(forms.ModelForm):

    class Meta:
        model = ParametrosConfiguracaoModel
        fields = '__all__'
