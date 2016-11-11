# coding: utf-8
from django import forms
from issem.models import BeneficioModel


class BeneficioForm(forms.ModelForm):
    data_inicial = forms.DateField(widget=forms.TextInput(attrs={'onfocus': 'limita_data_final()'}))

    class Meta:
        model = BeneficioModel
        fields = ('__all__')

    def clean_data_final(self):
        data_inicial = self.cleaned_data.get('data_inicial')
        data_final = self.cleaned_data.get('data_final')

        if not data_inicial:
            raise forms.ValidationError("Defina uma data inicial")

        if data_inicial <= data_final:
            return data_final
        else:
            raise forms.ValidationError("Data final deve ser após a data inicial")

    def clean_salario_maximo(self):
        salario_maximo = self.cleaned_data.get('salario_maximo')
        if int(salario_maximo) < 0:
            raise forms.ValidationError("Salário deve ser maior que zero")
        else:
            return salario_maximo