# coding: utf-8
from django import forms
from issem.models import ParametrosConsultaModel


class ConsultaParametrosForm(forms.ModelForm):

    class Meta:
        model = ParametrosConsultaModel
        fields = '__all__'
