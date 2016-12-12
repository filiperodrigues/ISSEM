#coding:utf-8
from django import forms
from issem.models import ContatoIssemModel


class ContatoIssemForm(forms.ModelForm):

    class Meta:
        model = ContatoIssemModel
        fields = '__all__'