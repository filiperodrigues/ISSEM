#coding:utf-8
from django import forms
from issem.models import Estado_Civil


class Estado_CivilForm(forms.ModelForm):
    class Meta:
        model = Estado_Civil
        fields = ('nome',)