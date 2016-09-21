#coding:utf-8
from django import forms
from issem.models.servidor import ServidorModel

class ServidorForm(forms.ModelForm):
    generos = (('M', 'Masculino',), ('F', 'Feminino',))
    sexo = forms.ChoiceField(widget=forms.RadioSelect, choices=generos)
    class Meta:
        model = ServidorModel
        fields = '__all__'
