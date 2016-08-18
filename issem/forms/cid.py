#coding:utf-8
from django import forms
from issem.models import Cid


class CidForm(forms.ModelForm):
    class Meta:
        model = Cid
        fields = ('id','descricao', 'status', 'gravidade')