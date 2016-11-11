# coding:utf-8
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django import forms
from django.contrib.auth.models import Group
from issem.forms.utilitarios.cpf_validator import CPF
from issem.models.estado import EstadoModel
from issem.models.pessoa import PessoaModel


class PessoaForm(forms.ModelForm):
    generos = (('M', 'Masculino',), ('F', 'Feminino',))
    sexo = forms.ChoiceField(required=False,
                             widget=forms.RadioSelect,
                             choices=generos,
                             )
    estado_natural = forms.ModelChoiceField(required=False,
                                            empty_label="Selecione um estado...",
                                            queryset=EstadoModel.objects.all(),
                                            widget=forms.Select(attrs={"onchange": "get_cidade_natural()", })
                                            )
    estado_atual = forms.ModelChoiceField(required=False,
                                          empty_label="Selecione um estado...",
                                          queryset=EstadoModel.objects.all(),
                                          widget=forms.Select(attrs={"onchange": "get_cidade_atual()", })
                                          )
    password = forms.CharField(widget=forms.PasswordInput())

    groups = forms.ModelChoiceField(required=True,
                                    empty_label="Selecione um departamento...",
                                    queryset=Group.objects.all())

    class Meta:
        model = PessoaModel
        fields = "__all__"

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')

        if CPF(cpf).isValid():
            return cpf
        else:
            raise forms.ValidationError("CPF inválido.")

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

    def save(self, commit=True):
        user = super(PessoaForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
