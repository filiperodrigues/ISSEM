# coding:utf-8
from issem.forms.validators.generic_validators import ValidarDataInicialFinal, ValidarDataNascimentoDependente
from issem.models.dependente import DependenteModel
from issem.forms.pessoa import CadPessoaForm, PessoaEditForm
from django import forms


class DependenteFormCad(CadPessoaForm):
    data_inicial = forms.DateField(widget=forms.TextInput(attrs={'onfocus': 'limita_data_final()', 'placeholder': 'DD/MM/AAAA'}))
    data_final = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA'}))
    password = forms.CharField(widget=forms.HiddenInput(attrs={'value': '111111'}))
    password_checker = forms.CharField(widget=forms.HiddenInput(attrs={'value': '111111'}))
    username = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = DependenteModel
        fields = '__all__'
        exclude = ('date_joined', 'is_active')

    def clean_data_final(self):
        return ValidarDataInicialFinal(self.cleaned_data.get('data_inicial'), self.cleaned_data.get('data_final'))

    def clean_tipo(self):
        if (str(self.cleaned_data.get('tipo')) != "Incapaz"):
            return ValidarDataNascimentoDependente(self.cleaned_data.get('data_nascimento'), self.cleaned_data.get('tipo'))
        return self.cleaned_data.get('tipo')


class DependenteFormEdit(PessoaEditForm):
    data_inicial = forms.DateField(widget=forms.DateInput(attrs={'onfocus': 'limita_data_final()'}))

    class Meta:
        model = DependenteModel
        fields = '__all__'
        exclude = ('date_joined', 'is_active', 'password', 'username')

    def clean_data_final(self):
        return ValidarDataInicialFinal(self.cleaned_data.get('data_inicial'), self.cleaned_data.get('data_final'))

