# coding: utf-8
from django import forms
from issem.models.servidor import ServidorModel

class ServidorForm(forms.ModelForm):
    generos = (('M', 'Masculino',), ('F', 'Feminino',))
    sexo = forms.ChoiceField(widget=forms.RadioSelect, choices=generos)

    ## TENTAR APLICAR CLASSE CSS PARA O CAMPO 'DOADOR'

    cpf = forms.CharField(widget=forms.TextInput(attrs={'maxlength':'14', 'OnKeyPress':"formatar('###.###.###-##', this)"}))
    telefone_residencial = forms.CharField(widget=forms.TextInput(attrs={'maxlength':'12'}))
    telefone_celular = forms.CharField(widget=forms.TextInput(attrs={'maxlength':'12'}))
    cep = forms.CharField(widget=forms.TextInput(attrs={'maxlength':'9', 'OnKeyPress':"formatar('#####-###', this)"}))

    class Meta:
        model = ServidorModel
        fields = '__all__'
