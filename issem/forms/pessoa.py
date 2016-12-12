# coding:utf-8
from django import forms
from issem.forms.utilitarios.cpf_validator import CPF
from issem.models.estado import EstadoModel
from issem.models.cidade import CidadeModel
from issem.models.pessoa import PessoaModel


class PessoaForm(forms.ModelForm):
    generos = (('M', 'Masculino',), ('F', 'Feminino',))
    sexo = forms.ChoiceField(required=False,
                             widget=forms.RadioSelect,
                             choices=generos,
                             )
    estados = EstadoModel.objects.all()
    cidades = CidadeModel.objects.all()
    estado_natural = forms.ModelChoiceField(required=False,
                                            empty_label="Selecione um estado",
                                            queryset=estados,
                                            widget=forms.Select(attrs={"onchange": "get_cidade_natural()",
                                                                       "class": "ui fluid search selection dropdown"})
                                            )
    estado_atual = forms.ModelChoiceField(required=False,
                                          empty_label="Selecione um estado",
                                          queryset=estados,
                                          widget=forms.Select(attrs={"onchange": "get_cidade_atual()",
                                                                     "class": "ui fluid search selection dropdown"})
                                          )
    cidade_natural = forms.ModelChoiceField(required=False,
                                            empty_label="Selecione uma cidade",
                                            queryset=cidades,
                                            widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
                                            )
    cidade_atual = forms.ModelChoiceField(required=False,
                                          empty_label="Selecione uma cidade",
                                          queryset=cidades,
                                          widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
                                          )
    password = forms.CharField(widget=forms.PasswordInput())
    password_checker = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = PessoaModel
        fields = "__all__"

    # def clean_cpf(self):
    #     cpf = self.cleaned_data.get('cpf')
    #
    #     if CPF(cpf).isValid():
    #         return cpf
    #     else:
    #         raise forms.ValidationError("CPF inválido.")

    def clean_password_checker(self):
        password = self.cleaned_data.get('password')
        password_checker = self.cleaned_data.get('password_checker')
        if password != password_checker:
            raise forms.ValidationError("Senhas diferentes")
        else:
            return password_checker

    def save(self, commit=True):
        user = super(PessoaForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
