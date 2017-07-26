#coding:utf-8
from django import forms
from issem.models.cargo import CargoModel


class CargoForm(forms.ModelForm):

    class Meta:
        model = CargoModel
        fields = '__all__'

