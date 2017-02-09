#coding:utf-8
from django import forms
from issem.models import ContatoIssemModel


class ContatoIssemForm(forms.ModelForm):

    class Meta:
        model = ContatoIssemModel
        fields = '__all__'

    def clean_departamento(self):
        nome = self.cleaned_data.get('nome')
        departamento = self.cleaned_data.get('departamento')

        if nome or departamento:
            return departamento
        else:
            raise forms.ValidationError("Nome ou Departamento é obrigatório.")

    def clean_cargo(self):
        nome = self.cleaned_data.get('nome')
        cargo = self.cleaned_data.get('cargo')

        if cargo:
            if nome:
                return cargo
            else:
                raise forms.ValidationError("Cargo deve estar relacionado à uma pessoa")
        return cargo