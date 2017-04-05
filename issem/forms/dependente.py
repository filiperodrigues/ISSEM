# coding:utf-8
from issem.forms.validators.generic_validators import ValidarDataInicialFinal
from issem.models.dependente import DependenteModel
from issem.forms.pessoa import CadPessoaForm, PessoaEditForm
from django import forms


class DependenteFormCad(CadPessoaForm):
    data_inicial = forms.DateField(widget=forms.TextInput(attrs={'onfocus': 'limita_data_final()'}))

    class Meta:
        model = DependenteModel
        fields = '__all__'
        exclude = ('date_joined', 'is_active')

    def clean_data_final(self):
        return ValidarDataInicialFinal(self.cleaned_data.get('data_inicial'), self.cleaned_data.get('data_final'))


class DependenteFormEdit(PessoaEditForm):
    data_inicial = forms.DateField(widget=forms.TextInput(attrs={'onfocus': 'limita_data_final()'}))

    class Meta:
        model = DependenteModel
        fields = '__all__'
        exclude = ('date_joined', 'is_active', 'password', 'username')

    def clean_data_final(self):
        return ValidarDataInicialFinal(self.cleaned_data.get('data_inicial'), self.cleaned_data.get('data_final'))