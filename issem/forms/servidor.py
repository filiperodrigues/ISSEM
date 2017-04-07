# coding:utf-8
from django import forms
from issem.forms.pessoa import CadPessoaForm, PessoaEditForm
from issem.forms.validators.generic_validators import ValidarDataNascimento
from issem.models.servidor import ServidorModel
from django.contrib.auth.models import Group


class ServidorFormCad(CadPessoaForm):
    groups = forms.ModelChoiceField(required=True,
                                    empty_label="Selecione um departamento...",
                                    queryset=Group.objects.all().exclude(name='Segurado').exclude(name='Dependente'),
                                    widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
                                    )

    class Meta:
        model = ServidorModel
        fields = '__all__'
        exclude = ('date_joined', 'is_active')

    def clean_crm(self):
        groups = self.cleaned_data.get('groups')
        crm = self.cleaned_data.get('crm')
        if str(groups) == "Tecnico":
            if crm:
                return crm
            else:
                raise forms.ValidationError("Digite um CRM.")
        else:
            return crm

    def clean_data_nascimento(self):
        return ValidarDataNascimento(self.cleaned_data.get('data_nascimento'))


class ServidorFormEdit(PessoaEditForm):
    # local_trabalho = forms.ModelChoiceField(required=False,
    #                                         empty_label="Selecione uma cidade",
    #                                         queryset=LocalTrabalhoModel.objects.all(),
    #                                         widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
    #                                         )
    groups = forms.ModelChoiceField(required=True,
                                    empty_label="Selecione um departamento...",
                                    queryset=Group.objects.all().exclude(name='Segurado').exclude(name='Dependente'),
                                    widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
                                    )
    class Meta:
        model = ServidorModel
        fields = '__all__'
        exclude = ('date_joined', 'is_active', 'password', 'username')

    def clean_crm(self):
        groups = self.cleaned_data.get('groups')
        crm = self.cleaned_data.get('crm')
        if str(groups) == "Tecnico":
            if crm:
                return crm
            else:
                raise forms.ValidationError("Digite um CRM.")
        else:
            return crm

    def clean_data_nascimento(self):
        return ValidarDataNascimento(self.cleaned_data.get('data_nascimento'))