# coding:utf-8
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django import forms
from issem.models.segurado import SeguradoModel
from issem.models.local_trabalho import LocalTrabalhoModel
from issem.forms.pessoa import PessoaForm


class SeguradoForm(PessoaForm):
    local_trabalho = forms.ModelChoiceField(required=False,
                                            empty_label="Selecione uma cidade",
                                            queryset=LocalTrabalhoModel.objects.all(),
                                            widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
                                            )
    groups = forms.CharField(required=False)

    class Meta:
        model = SeguradoModel
        fields = '__all__'
        exclude = ('date_joined', 'is_active')

    def clean_data_nascimento(self):
        data_nascimento = self.cleaned_data.get('data_nascimento')
        data_gerada = datetime.now() - relativedelta(years=18)
        data_gerada = data_gerada.date()
        if data_nascimento == None:
            raise forms.ValidationError("Este campo é obrigatório.")
        elif data_nascimento <= data_gerada:
            return data_nascimento
        else:
            raise forms.ValidationError("Deve ter mais que 18 anos")