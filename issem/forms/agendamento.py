# coding:utf-8
from django import forms
from issem.models.agendamento import AgendamentoModel


class AgendamentoForm(forms.ModelForm):
    hora_pericia = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'class': 'time-pick'}),
                                   help_text='ex: 10:30AM')

    class Meta:
        model = AgendamentoModel
        fields = '__all__'
