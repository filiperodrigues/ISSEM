#coding:utf-8
from django import forms
from issem.models import CidModel


class CidForm(forms.ModelForm):

    class Meta:
        model = CidModel
        fields = ('id','descricao', 'status', 'gravidade')