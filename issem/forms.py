from django import forms
from issem.models import Departamento, Cid

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ('nome_departamento',)

class CidForm(forms.ModelForm):

    class Meta:
        model = Cid
        fields = ('id','descricao_cid', 'status', 'gravidade_cid')

