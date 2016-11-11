# coding:utf-8
from django import forms
from issem.models.requerimento import RequerimentoModel
from issem.models.consulta_parametros import ConsultaParametrosModel
from issem.models.agendamento import AgendamentoModel
from issem.models.segurado import SeguradoModel
from datetime import date


class RequerimentoForm(forms.ModelForm):
    data_inicio_afastamento = forms.DateField(widget=forms.TextInput(attrs={'onfocus': 'limita_data_final_afastamento()'}))
    segurado = forms.ModelChoiceField(
                                queryset=SeguradoModel.objects.all(),
                                widget=forms.Select(attrs={"class": "ui fluid search selection dropdown", })
                                )

    class Meta:
        model = RequerimentoModel
        fields = '__all__'

    def clean_data_final_afastamento(self):
        data_inicio_afastamento = self.cleaned_data.get('data_inicio_afastamento')
        data_final_afastamento = self.cleaned_data.get('data_final_afastamento')

        if not data_inicio_afastamento:
            raise forms.ValidationError("Defina uma data de início")

        if data_inicio_afastamento <= data_final_afastamento:
            return data_final_afastamento
        else:
            raise forms.ValidationError("Data final deve ser após a data de início")

    # def clean_data_requerimento(self):
    #     data_requerimento = date.today()
    #     self.cleaned_data['data_requerimento'] = data_requerimento
    #     return self.cleaned_data['data_requerimento']
