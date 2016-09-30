#coding:utf-8
from django import forms
from issem.models.segurado import SeguradoModel
from issem.models.estado import EstadoModel
from cpf_validator import CPF


class SeguradoForm(forms.ModelForm):
    generos = (('M', 'Masculino',), ('F', 'Feminino',))
    sexo = forms.ChoiceField(required=False,
                             widget=forms.RadioSelect,
                             choices=generos,
                             )
    estado_natural = forms.ModelChoiceField(required=False,
                                            empty_label="Selecione um estado...",
                                            queryset=EstadoModel.objects.all(),
                                            widget=forms.Select(attrs={"onchange": "get_cidade_natural()",})
                                            )
    estado_atual = forms.ModelChoiceField(required=False,
                                          empty_label="Selecione um estado...",
                                          queryset=EstadoModel.objects.all(),
                                          widget=forms.Select(attrs={"onchange": "get_cidade_atual()",})
                                          )

    class Meta:
        model = SeguradoModel
        fields = '__all__'

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')

        if CPF(cpf).isValid():
            return cpf
        else:
            raise forms.ValidationError("CPF inválido.")