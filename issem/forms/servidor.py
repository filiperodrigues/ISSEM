#coding:utf-8
from django import forms
from issem.models.servidor import ServidorModel
from issem.models.estado import EstadoModel


class ServidorForm(forms.ModelForm):
    # nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'somente_letras'}))
    # cpf = forms.CharField(widget=forms.TextInput(attrs={'class': 'cpf', 'maxlength': '14'}))
    # rg = forms.CharField(widget=forms.TextInput(attrs={'class': 'rg'}))
    # data_nascimento = forms.CharField(widget=forms.TextInput(attrs={'class': 'data'}))
    # telefone_residencial = forms.CharField(widget=forms.TextInput(attrs={'class': 'fone_ddd'}))
    # telefone_celular = forms.CharField(widget=forms.TextInput(attrs={'class': 'fone_ddd'}))
    # cep = forms.CharField(widget=forms.TextInput(attrs={'class': 'cep'}))
    # numero_endereco = forms.CharField(widget=forms.TextInput(attrs={'class': 'n_endereco'}))
    # nome_pai = forms.CharField(widget=forms.TextInput(attrs={'class': 'somente_letras'}))
    generos = (('M', 'Masculino',), ('F', 'Feminino',))
    sexo = forms.ChoiceField(required=False,
        widget=forms.RadioSelect,
        choices=generos,
    )
    estado_natural = forms.ModelChoiceField(required=False,
        empty_label="Selecione um estado...",
        queryset=EstadoModel.objects.all(),
        widget=forms.Select(attrs={"onchange": "get_cidade_natural()",})
    )
    estado_atual = forms.ModelChoiceField(required=False,
        empty_label="Selecione um estado...",
        queryset=EstadoModel.objects.all(),
        widget=forms.Select(attrs={"onchange": "get_cidade_atual()",})
    )

    class Meta:
        model = ServidorModel
        fields = '__all__'
