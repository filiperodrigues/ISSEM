# coding:utf-8
from django import forms

from issem.forms.validators.generic_validators import ValidarDataInicialFinal
from issem.models.requerimento import RequerimentoModel
from issem.models.segurado import SeguradoModel
from datetime import date


class RequerimentoForm(forms.ModelForm):
    data_inicio_afastamento = forms.DateField(widget=forms.TextInput(attrs={'onfocus': 'limita_data_final_afastamento()'}))
    segurado = forms.ModelChoiceField(
                                queryset=SeguradoModel.objects.all(),
                                widget=forms.Select(attrs={"class": "ui fluid search selection dropdown", })
                                )

    class Meta:
        model = RequerimentoModel
        fields = '__all__'

    # def clean_data_final_afastamento(self):
    #     print("ENTRANDO NO CLEAN !!!")
    #     print(self.cleaned_data.get('data_inicial'))
    #     return ValidarDataInicialFinal(self.cleaned_data.get('data_inicial'), self.cleaned_data.get('data_final'))

    def clean_data_requerimento(self):
        data_requerimento = date.today()
        self.cleaned_data['data_requerimento'] = data_requerimento
        return self.cleaned_data['data_requerimento']
