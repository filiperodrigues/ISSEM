# coding: utf-8
from django import forms
from issem.models import BeneficioModel


class BeneficioForm(forms.ModelForm):
    data_inicial = forms.DateField(widget=forms.TextInput(attrs={'onfocus': 'change_life()'}))

    class Meta:
        model = BeneficioModel
        fields = ('__all__')

