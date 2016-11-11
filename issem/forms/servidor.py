# coding:utf-8
from django import forms
from issem.forms.pessoa import PessoaForm
from issem.models.servidor import ServidorModel
from django.contrib.auth.models import Group


class ServidorForm(PessoaForm):
    groups = forms.ModelChoiceField(required=True,
                                    empty_label="Selecione um departamento...",
                                    queryset=Group.objects.all().exclude(name='Segurado'),
                                    widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
                                    )
    class Meta:
        model = ServidorModel
        fields = '__all__'
        exclude = ('date_joined', 'is_active')

    def clean_crm(self):
        groups = self.cleaned_data.get('groups')
        crm = self.cleaned_data.get('crm')
        if str(groups) == "Médico":
            if crm:
                return crm
            else:
                raise forms.ValidationError("Digite um CRM.")
        else:
            return crm