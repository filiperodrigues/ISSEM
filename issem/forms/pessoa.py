# coding:utf-8
from django import forms
from django.contrib.auth.management import get_default_username

from issem.forms.validators.cpf_validator import ValidarCPF
from issem.forms.validators.generic_validators import ValidarPassword, ValidarTamanhoPassword
from issem.models import CargoModel
from issem.models.estado import EstadoModel
from issem.models.cidade import CidadeModel
from issem.models.pessoa import PessoaModel


class CadPessoaForm(forms.ModelForm):
    cargo = forms.ModelChoiceField(required=False,
                                   queryset=CargoModel.objects.all(),
                                   empty_label="Selecione um cargo",
                                   widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
                                   )
    generos = (('M', 'Masculino',), ('F', 'Feminino',))
    sexo = forms.ChoiceField(required=False,
                             widget=forms.RadioSelect,
                             choices=generos,
                             )
    estados = EstadoModel.objects.all()
    cidades = CidadeModel.objects.filter(id=0)
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
    password = forms.CharField(required=False, widget=forms.PasswordInput())
    password_checker = forms.CharField(required=False, widget=forms.PasswordInput())
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA'}))


    class Meta:
        model = PessoaModel
        fields = "__all__"

    # def clean_cpf(self):
    #     return ValidarCPF(self.cleaned_data.get('cpf'))

    # def clean_password(self):
    #     return ValidarTamanhoPassword(self.cleaned_data['password'])
    #
    # def clean_password_checker(self):
    #     return ValidarPassword(self.cleaned_data.get('password'), self.cleaned_data.get('password_checker'))

    def save(self, commit=True):
        user = super(CadPessoaForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()


class PessoaEditForm(forms.ModelForm):
    cargo = forms.ModelChoiceField(required=False,
                                   queryset=CargoModel.objects.all(),
                                   empty_label="Selecione um cargo",
                                   widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
                                   )
    generos = (('M', 'Masculino',), ('F', 'Feminino',))
    sexo = forms.ChoiceField(required=False,
                             widget=forms.RadioSelect,
                             choices=generos,
                             )
    estados = EstadoModel.objects.all()
    cidades = CidadeModel.objects.filter(id=0)
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
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA'}))


    class Meta:
        model = PessoaModel
        fields = "__all__"

    # def clean_cpf(self):
    #     return ValidarCPF(self.cleaned_data.get('cpf'))

    def save(self, commit=True):
        try:
            user = super(PessoaEditForm, self).save(commit=False)
            if commit:
                user.save()
        except:
            pass


class PessoaPasswordForm(forms.ModelForm):
    password = forms.CharField(required=False, widget=forms.PasswordInput())
    password_checker = forms.CharField(required=False, widget=forms.PasswordInput())

    class Meta:
        model = PessoaModel
        fields = ['password']

    # def clean_password(self):
    #     return ValidarTamanhoPassword(self.cleaned_data['password'])
    #
    # def clean_password_checker(self):
    #     return ValidarPassword(self.cleaned_data.get('password'), self.cleaned_data.get('password_checker'))

    def save(self, commit=True):
        user = super(PessoaPasswordForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
