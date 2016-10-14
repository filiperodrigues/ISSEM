# coding:utf-8
from django import forms
from issem.models.agendamento import AgendamentoModel


class AgendamentoForm(forms.ModelForm):
    tipo_orgao = (('PMJS', 'PMJS',), ('Samae', 'Samae',), ('Câmara', 'Câmara',), ('Issem', 'Issem',))
    orgao = forms.ChoiceField(required=False, widget=forms.Select, choices=tipo_orgao)

    class Meta:
        model = AgendamentoModel
        fields = '__all__'