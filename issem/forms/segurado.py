#coding:utf-8
from django import forms
from issem.models.segurado import SeguradoModel
from localflavor.br.forms import BRCPFField
from input_mask.contrib.localflavor.br.widgets import BRCPFInput


class SeguradoForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={'required' :'required',}))
    email = forms.CharField(widget=forms.TextInput(attrs={'required' :'required',}))
    cpf = forms.CharField(widget=forms.TextInput(attrs={
        'required' :'required',
    }))
    rg = forms.CharField(widget=forms.TextInput(attrs={'required':'required',}))
    class Meta:
        model = SeguradoModel
        fields = '__all__'
