# coding: utf-8
from django import forms
from issem.forms.validators.generic_validators import ValidarDataInicialFinal
from issem.models.beneficio import BeneficioModel


class BeneficioForm(forms.ModelForm):
    # data_inicial = forms.DateField(widget=forms.TextInput(attrs={'onfocus': 'limita_data_final()'}))
    data_portaria = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA'}))

    data_inicial = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA'}))

    data_final = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA'}))

    data_retorno = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA'}))

    data_pericia = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA'}))

    class Meta:
        model = BeneficioModel
        fields = ('__all__')

    def clean_data_final(self):
        return ValidarDataInicialFinal(self.cleaned_data.get('data_inicial'), self.cleaned_data.get('data_final'))

    def clean_salario_maximo(self):
        salario_maximo = self.cleaned_data.get('salario_maximo')
        if int(salario_maximo) < 0:
            raise forms.ValidationError("Salário deve ser maior que zero")
        else:
            return salario_maximo
