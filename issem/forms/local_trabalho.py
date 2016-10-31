# coding:utf-8
from django import forms

from issem.models.estado import EstadoModel
from issem.forms.utilitarios.cnpj_validator import CNPJ
from issem.models.local_trabalho import LocalTrabalhoModel


class LocalTrabalhoForm(forms.ModelForm):
    estados = forms.ModelChoiceField(required=False,
                                     empty_label="Selecione um estado...",
                                     queryset=EstadoModel.objects.all(),
                                     widget=forms.Select(attrs={"onchange": "get_cidade_local_trabalho()"})
                                     )

    class Meta:
        model = LocalTrabalhoModel
        fields = '__all__'

    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
        if CNPJ().validate(cnpj):
            return cnpj
        else:
            raise forms.ValidationError("CNPJ inválido")
