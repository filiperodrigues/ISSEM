# coding: utf-8
from django import forms
from issem.models import ConsultaParametrosModel


class ConsultaParametrosForm(forms.ModelForm):

    class Meta:
        model = ConsultaParametrosModel
        fields = '__all__'
