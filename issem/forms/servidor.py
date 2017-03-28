# coding:utf-8
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django import forms
from issem.forms.pessoa import CadPessoaForm, PessoaEditForm
from issem.models.servidor import ServidorModel
from django.contrib.auth.models import Group


class ServidorFormCad(CadPessoaForm):
    groups = forms.ModelChoiceField(required=True,
                                    empty_label="Selecione um departamento...",
                                    queryset=Group.objects.all().exclude(name='Segurado').exclude(name='Dependente'),
                                    widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
                                    )

    class Meta:
        model = ServidorModel
        fields = '__all__'
        exclude = ('date_joined', 'is_active')

    def clean_crm(self):
        groups = self.cleaned_data.get('groups')
        crm = self.cleaned_data.get('crm')
        if str(groups) == "Técnico":
            if crm:
                return crm
            else:
                raise forms.ValidationError("Digite um CRM.")
        else:
            return crm

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

class ServidorFormEdit(PessoaEditForm):
    # local_trabalho = forms.ModelChoiceField(required=False,
    #                                         empty_label="Selecione uma cidade",
    #                                         queryset=LocalTrabalhoModel.objects.all(),
    #                                         widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
    #                                         )
    groups = forms.ModelChoiceField(required=True,
                                    empty_label="Selecione um departamento...",
                                    queryset=Group.objects.all().exclude(name='Segurado').exclude(name='Dependente'),
                                    widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
                                    )
    class Meta:
        model = ServidorModel
        fields = '__all__'
        exclude = ('date_joined', 'is_active', 'password', 'username')

    def clean_crm(self):
        groups = self.cleaned_data.get('groups')
        crm = self.cleaned_data.get('crm')
        if str(groups) == "Técnico":
            if crm:
                return crm
            else:
                raise forms.ValidationError("Digite um CRM.")
        else:
            return crm

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