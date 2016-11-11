# coding:utf-8
from issem.models.dependente import DependenteModel
from issem.forms.pessoa import PessoaForm
from django import forms


class DependenteForm(PessoaForm):
    data_inicial = forms.DateField(widget=forms.TextInput(attrs={'onfocus': 'limita_data_final()'}))

    class Meta:
        model = DependenteModel
        fields = '__all__'
        exclude = ('date_joined', 'is_active', 'groups', 'user', 'password',)

    def clean_data_final(self):
        data_inicial = self.cleaned_data.get('data_inicial')
        data_final = self.cleaned_data.get('data_final')

        if not data_inicial:
            raise forms.ValidationError("Defina uma data inicial")

        if data_inicial <= data_final:
            return data_final
        else:
            raise forms.ValidationError("Data final deve ser após a data inicial")