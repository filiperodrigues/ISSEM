# coding: utf-8
from django import forms
from issem.models.beneficio import BeneficioModel
from issem.models.cid import CidModel
from issem.models.laudo import LaudoModel
from issem.models.segurado import SeguradoModel
from issem.models.procedimento_medico import ProcedimentoMedicoModel
from issem.models.requerimento import RequerimentoModel


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
                                                 empty_label="Pesquise um procedimento",
                                                 queryset=ProcedimentoMedicoModel.objects.filter(id=0, excluido=False),
                                                 widget=forms.SelectMultiple(
                                                     attrs={"class": "ui fluid search selection dropdown"})
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
