# coding: utf-8
from django import forms
from issem.models import BeneficioModel
from issem.models import CidModel
from issem.models import LaudoModel, SeguradoModel
from issem.models import ProcedimentoMedicoModel
from issem.models import RequerimentoModel


class LaudoForm(forms.ModelForm):
    segurado = forms.ModelChoiceField(required=True,
                                      empty_label="Selecione um segurado",
                                      queryset=SeguradoModel.objects.filter(excluido=False),
                                      widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
                                      )
    requerimento = forms.ModelChoiceField(required=True,
                                          empty_label="Selecione um requerimento",
                                          queryset=RequerimentoModel.objects.all(),
                                          widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
                                          )
    beneficio = forms.ModelChoiceField(required=True,
                                       empty_label="Selecione um benefício",
                                       queryset=BeneficioModel.objects.filter(excluido=False),
                                       widget=forms.Select(attrs={"class": "ui fluid search selection dropdown"})
                                       )
    procedimento_medico = forms.ModelChoiceField(required=True,
                                                 empty_label="Selecione um procedimento",
                                                 queryset=ProcedimentoMedicoModel.objects.filter(excluido=False),
                                                 widget=forms.Select(
                                                 # widget=forms.SelectMultiple(
                                                     attrs={"onchange": "get_procedimentos_medicos()",
                                                            "class": "ui fluid search selection dropdown"})
                                                 )
    cid = forms.ModelChoiceField(required=True,
                                 empty_label="Selecione um CID",
                                 queryset=CidModel.objects.filter(excluido=False),
                                 widget=forms.SelectMultiple(attrs={"class": "ui fluid search selection dropdown"})
                                 )
    historico_doenca = forms.CharField(required=True,
                                       widget=forms.Textarea(attrs={"rows": "1"}))
    anamnese = forms.CharField(required=True,
                               widget=forms.Textarea(attrs={"rows": "5"}))
    observacoes = forms.CharField(required=True,
                                  widget=forms.Textarea(attrs={"rows": "1"}))
    exames_apresentados = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = LaudoModel
        fields = '__all__'
