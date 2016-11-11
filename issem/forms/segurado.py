# coding:utf-8
from django import forms
from issem.models.segurado import SeguradoModel
from issem.models.local_trabalho import LocalTrabalhoModel
from issem.forms.pessoa import PessoaForm


class SeguradoForm(PessoaForm):
    local_trabalho = forms.ModelChoiceField(required=False,
                                            empty_label="Selecione uma cidade",
                                            queryset=LocalTrabalhoModel.objects.all(),
                                            widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
                                            )
    groups = forms.CharField(required=False)

    class Meta:
        model = SeguradoModel
        fields = '__all__'
        exclude = ('date_joined', 'is_active')
