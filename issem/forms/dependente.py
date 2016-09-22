#coding:utf-8
from django import forms
from issem.models.dependente import DependenteModel


class DependenteForm(forms.ModelForm):
    generos = (('M', 'Masculino',), ('F', 'Feminino',))
    sexo = forms.ChoiceField(widget=forms.RadioSelect, choices=generos)
    class Meta:
        model = DependenteModel
        fields = '__all__'