#coding:utf-8
from django import forms
from issem.models import TipoLaudoModel


class TipoLaudoForm(forms.ModelForm):

    class Meta:
        model = TipoLaudoModel
        fields = '__all__'