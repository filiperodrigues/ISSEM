#coding:utf-8
from django import forms
from issem.models.segurado import SeguradoModel


class SeguradoForm(forms.ModelForm):
    generos = (('M', 'Masculino',), ('F', 'Feminino',))
    sexo = forms.ChoiceField(widget=forms.RadioSelect, choices=generos)
    class Meta:
        model = SeguradoModel
        fields = '__all__'
