#coding:utf-8
from django import forms
from issem.models import Cargo


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ('nome',)

