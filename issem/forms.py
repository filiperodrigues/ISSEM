from django import forms
from issem.models import Departamento, Cid, Procedimento_Medico, Beneficios

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
        fields = ('codigo', 'descricao', 'porte', 'custo_op')

class BeneficiosForm(forms.ModelForm):
    class Meta:
        model = Beneficios
        fields = ('concessao', 'dt_inicial', 'dt_final', 'dt_retorno', 'dt_pericia', 'descricao', 'nr_portaria', 'dt_portaria', 'salario_max', 'observacao', 'carencia')
