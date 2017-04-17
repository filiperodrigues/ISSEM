# coding: utf-8
from django import forms
from issem.models import LaudoModel, SeguradoModel


class LaudoForm(forms.ModelForm):
    segurados = SeguradoModel.objects.filter(excluido=False)
    segurado = forms.ModelChoiceField(required=True,
                                            empty_label="Selecione um segurado",
                                            queryset=segurados,
                                            widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
                                            )

    class Meta:
        model = LaudoModel
        fields = '__all__'
