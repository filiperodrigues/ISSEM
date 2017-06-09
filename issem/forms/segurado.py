# coding:utf-8
from django import forms

from issem.forms.validators.generic_validators import ValidarDataNascimento
from issem.models.segurado import SeguradoModel
from issem.models.local_trabalho import LocalTrabalhoModel
from issem.forms.pessoa import CadPessoaForm, PessoaEditForm


class SeguradoFormCad(CadPessoaForm):
    local_trabalho = forms.ModelChoiceField(required=False,
                                            empty_label="Selecione uma cidade",
                                            queryset=LocalTrabalhoModel.objects.all(),
                                            widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
                                            )
    groups = forms.CharField(required=False)
    data_admissao = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA'}))
    email = forms.EmailField(required=True)

    class Meta:
        model = SeguradoModel
        fields = '__all__'
        exclude = ('date_joined', 'is_active')

    def clean_data_nascimento(self):
        return ValidarDataNascimento(self.cleaned_data.get('data_nascimento'))


class SeguradoFormEdit(PessoaEditForm):
    local_trabalho = forms.ModelChoiceField(required=False,
                                            empty_label="Selecione uma cidade",
                                            queryset=LocalTrabalhoModel.objects.all(),
                                            widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
                                            )
    groups = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    data_admissao = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA'}))

    class Meta:
        model = SeguradoModel
        fields = '__all__'
        exclude = ('date_joined', 'is_active', 'password', 'username')

    def clean_data_nascimento(self):
        return ValidarDataNascimento(self.cleaned_data.get('data_nascimento'))

    def __init__(self, *args, **kwargs):
        try:
            id = kwargs.pop('id')
            segurado = SeguradoModel.objects.get(pk=id)
            super(SeguradoFormEdit, self).__init__(*args, **kwargs)

            if self.fields['estado_natural']:
                self.fields['estado_natural'].initial = segurado.cidade_natural.uf.id
            if self.fields['estado_atual']:
                self.fields['estado_atual'].initial = segurado.cidade_atual.uf.id
        except:
            pass
