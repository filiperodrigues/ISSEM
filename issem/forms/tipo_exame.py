#coding:utf-8
from django import forms
from issem.models import TipoExameModel


class TipoExameForm(forms.ModelForm):

    class Meta:
        model = TipoExameModel
        fields = '__all__'