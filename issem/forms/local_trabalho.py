# coding:utf-8
from django import forms
from issem.models.local_trabalho import LocalTrabalhoModel


class LocalTrabalhoForm(forms.ModelForm):

    class Meta:
        model = LocalTrabalhoModel
        fields = ('nome','cnpj','endereco','numero_endereco','cidade','bairro','cep','complemento','secretaria')
