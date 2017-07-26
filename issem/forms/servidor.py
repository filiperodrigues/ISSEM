# coding:utf-8
from django import forms
from issem.forms.pessoa import CadPessoaForm, PessoaEditForm
from issem.forms.validators.generic_validators import ValidarDataNascimento, ValidaCRM, ValidarTamanhoPassword, \
    ValidarPassword, ValidaEmail
from issem.models.funcao import FuncaoModel
from issem.models.servidor import ServidorModel
from django.contrib.auth.models import Group


class ServidorFormCad(CadPessoaForm):
    groups = forms.ModelChoiceField(required=True,
                                    empty_label="Selecione um departamento...",
                                    queryset=Group.objects.all().exclude(name='Segurado').exclude(name='Dependente'),
                                    widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
                                    )
    email = forms.EmailField(required=True)
    funcao = forms.ModelChoiceField(required=False,
                                    queryset=FuncaoModel.objects.all(),
                                    empty_label="Selecione uma função",
                                    widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
                                    )

    class Meta:
        model = ServidorModel
        fields = '__all__'
        exclude = ('date_joined', 'is_active')

    def clean_password(self):
        return ValidarTamanhoPassword(self.cleaned_data['password'])

    def clean_password_checker(self):
        return ValidarPassword(self.cleaned_data.get('password'), self.cleaned_data.get('password_checker'))

    def clean_crm(self):
        return ValidaCRM(self.cleaned_data.get('crm'), self.cleaned_data.get('groups'))

    def clean_email(self):
        return ValidaEmail(self.cleaned_data['email'], self.instance.id)

    def clean_data_nascimento(self):
        return ValidarDataNascimento(self.cleaned_data.get('data_nascimento'))


class ServidorFormEdit(PessoaEditForm):
    email = forms.EmailField(required=True)
    funcao = forms.ModelChoiceField(required=False,
                                    queryset=FuncaoModel.objects.all(),
                                    empty_label="Selecione uma função",
                                    widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
                                    )

    class Meta:
        model = ServidorModel
        fields = '__all__'
        exclude = ('date_joined', 'is_active', 'password', 'username', 'groups')

    def clean_crm(self):
        return ValidaCRM(self.cleaned_data.get('crm'), self.cleaned_data.get('groups'))

    def clean_data_nascimento(self):
        return ValidarDataNascimento(self.cleaned_data.get('data_nascimento'))

    def clean_email(self):
        return ValidaEmail(self.cleaned_data['email'], self.instance.id)

    def __init__(self, *args, **kwargs):
        try:
            # TODO Parte comentada é para a futura modelagem
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
