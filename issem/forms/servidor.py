# coding:utf-8
from django import forms
from issem.forms.pessoa import CadPessoaForm, PessoaEditForm
from issem.forms.validators.generic_validators import ValidarDataNascimento
from issem.models.servidor import ServidorModel
from django.contrib.auth.models import Group


class ServidorFormCad(CadPessoaForm):
    groups = forms.ModelChoiceField(required=True,
                                    empty_label="Selecione um departamento...",
                                    queryset=Group.objects.all().exclude(name='Segurado').exclude(name='Dependente'),
                                    widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
                                    )
    email = forms.EmailField(required=True)

    class Meta:
        model = ServidorModel
        fields = '__all__'
        exclude = ('date_joined', 'is_active')

    def clean_crm(self):
        groups = self.cleaned_data.get('groups')
        crm = self.cleaned_data.get('crm')
        if str(groups) == "Tecnico":
            if crm:
                return crm
            else:
                raise forms.ValidationError("Digite um CRM.")
        else:
            return crm

    def clean_data_nascimento(self):
        return ValidarDataNascimento(self.cleaned_data.get('data_nascimento'))


class ServidorFormEdit(PessoaEditForm):
    groups = forms.ModelChoiceField(required=True,
                                    empty_label="Selecione um departamento...",
                                    queryset=Group.objects.all().exclude(name='Segurado').exclude(name='Dependente'),
                                    widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
                                    )
    email = forms.EmailField(required=True)

    class Meta:
        model = ServidorModel
        fields = '__all__'
        exclude = ('date_joined', 'is_active', 'password', 'username', 'groups')

    def clean_crm(self):
        groups = self.cleaned_data.get('groups')
        crm = self.cleaned_data.get('crm')
        if str(groups) == "Tecnico":
            if crm:
                return crm
            else:
                raise forms.ValidationError("Digite um CRM.")
        else:
            return crm

    def clean_data_nascimento(self):
        return ValidarDataNascimento(self.cleaned_data.get('data_nascimento'))

    def __init__(self, *args, **kwargs):
        try:
            #TODO Parte comentada é para a futura modelagem
            id = kwargs.pop('id')
            servidor = ServidorModel.objects.get(id=id)
            # departamento = Group.objects.filter(name__in=['Administrativo','Tecnico'])
            super(ServidorFormEdit, self).__init__(*args, **kwargs)
            if self.fields['estado_natural']:
                self.fields['estado_natural'].initial = servidor.cidade_natural.uf.id
            if self.fields['estado_atual']:
                self.fields['estado_atual'].initial = servidor.cidade_atual.uf.id

            # self.fields['groups'] = forms.ModelMultipleChoiceField(queryset=departamento,
            #                                                       #initial=departamento.filter(pk='1'),
            #                                                       initial=servidor.groups.all()[0].id,
            #                                                        widget=forms.SelectMultiple(),
            #                                                        label='',
            #                                                        required=False,
            #
            #                                                        )
        except:
            pass