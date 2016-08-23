# coding:utf-8
from django import forms
from issem.models.local_trabalho import Local_Trabalho


class Local_TrabalhoForm(forms.ModelForm):
    class Meta:
        model = Local_Trabalho
        fields = ('nome','cnpj','endereco','numero_endereco','cidade','bairro','cep','complemento')
