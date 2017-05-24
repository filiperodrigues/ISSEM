# coding:utf-8
from django import forms
from issem.models.agendamento import AgendamentoModel


class AgendamentoForm(forms.ModelForm):
    hora_pericia = forms.TimeField(widget=forms.widgets.TimeInput(attrs={'class': 'time-pick', 'placeholder': 'HH:MM'}),
                                   help_text='ex: 10:30AM')

    data_pericia = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA'}))

    class Meta:
        model = AgendamentoModel
        fields = '__all__'
