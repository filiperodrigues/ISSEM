# coding:utf-8
from django import forms
from issem.models.cid import CidModel


class CidForm(forms.ModelForm):

    class Meta:
        model = CidModel
        fields = '__all__'