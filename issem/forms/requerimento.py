# coding:utf-8
from django import forms
from issem.models.requerimento import RequerimentoModel
from issem.models.consulta_parametros import ConsultaParametrosModel
from issem.models.agendamento import AgendamentoModel
from datetime import date


class RequerimentoForm(forms.ModelForm):

    class Meta:
        model = RequerimentoModel
        fields = '__all__'

    def clean_data_requerimento(self):
        data_requerimento = date.today()
        self.cleaned_data['data_requerimento'] = data_requerimento
        return self.cleaned_data['data_requerimento']
