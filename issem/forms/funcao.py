#coding:utf-8
from django import forms
from issem.models import FuncaoModel


class FuncaoForm(forms.ModelForm):

    class Meta:
        model = FuncaoModel
        fields = ('nome',)
