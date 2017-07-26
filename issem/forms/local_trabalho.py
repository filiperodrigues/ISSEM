# coding:utf-8
from django import forms
from issem.models.cidade import CidadeModel
from issem.models.estado import EstadoModel
from issem.forms.validators.cnpj_validator import ValidarCNPJ
from issem.models.local_trabalho import LocalTrabalhoModel
from issem.models.secretaria import SecretariaModel


class LocalTrabalhoForm(forms.ModelForm):
    estados = forms.ModelChoiceField(required=False,
                                     empty_label="Selecione um estado",
                                     queryset=EstadoModel.objects.all(),
                                     widget=forms.Select(attrs={"onchange": "get_cidade_local_trabalho()",
                                                                "class": "ui fluid search selection dropdown"})
                                     )
    cidade = forms.ModelChoiceField(required=False,
                                    empty_label="Selecione uma cidade",
                                    queryset=CidadeModel.objects.all(),
                                    widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
                                    )
    secretaria = forms.ModelChoiceField(required=False,
                                        empty_label="Selecione uma secretaria",
                                        queryset=SecretariaModel.objects.all(),
                                        widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
                                        )

    class Meta:
        model = LocalTrabalhoModel
        fields = '__all__'

    def clean_cnpj(self):
        return ValidarCNPJ(self.cleaned_data.get('cnpj'))
