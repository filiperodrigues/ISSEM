#coding:utf-8
from django import forms
from issem.models import Departamento, Cid, Procedimento_Medico, Beneficio, Funcao, Cargo, Tipo_Dependente, Tipo_Exame

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ('nome',)

class CidForm(forms.ModelForm):
    class Meta:
        model = Cid
        fields = ('id','descricao', 'status', 'gravidade')

class Procedimento_MedicoForm(forms.ModelForm):
    class Meta:
        model = Procedimento_Medico
        fields = ('codigo', 'descricao', 'porte', 'custo_operacao')

class BeneficioForm(forms.ModelForm):
    class Meta:
        model = Beneficio
        fields = ('concessao', 'data_inicial', 'data_final', 'data_retorno', 'data_pericia', 'descricao', 'numero_portaria', 'data_portaria', 'salario_maximo', 'observacao', 'carencia')

class FuncaoForm(forms.ModelForm):
    class Meta:
        model = Funcao
        fields = ('nome',)

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ('nome',)

class Tipo_DependenteForm(forms.ModelForm):
    class Meta:
        model = Tipo_Dependente
        fields = ('nome',)

class Tipo_ExameForm(forms.ModelForm):
    class Meta:
        model = Tipo_Exame
        fields = ('nome', 'observacao',)