# coding: utf-8
from django import forms
from issem.models.servidor import ServidorModel
from issem.models.estado import EstadoModel


class ServidorForm(forms.ModelForm):
    generos = (('M', 'Masculino',), ('F', 'Feminino',))
    sexo = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=generos
    )
    estado_natural = forms.ModelChoiceField(
        empty_label="Selecione um estado...",
        queryset=EstadoModel.objects.all(),
        widget=forms.Select(attrs={"onchange": "get_cidade_natural()",})
    )
    estado_atual = forms.ModelChoiceField(
        empty_label="Selecione um estado...",
        queryset=EstadoModel.objects.all(),
        widget=forms.Select(attrs={"onchange": "get_cidade_atual()",})
    )

    cpf = forms.CharField(
        widget=forms.TextInput(attrs={'maxlength': '14', 'OnKeyPress': "formatar('###.###.###-##', this)"}))
    telefone_residencial = forms.CharField(widget=forms.TextInput(attrs={'maxlength': '12'}))
    telefone_celular = forms.CharField(widget=forms.TextInput(attrs={'maxlength': '12'}))
    cep = forms.CharField(widget=forms.TextInput(attrs={'maxlength': '9', 'OnKeyPress': "formatar('#####-###', this)"}))

    class Meta:
        model = ServidorModel
        fields = '__all__'