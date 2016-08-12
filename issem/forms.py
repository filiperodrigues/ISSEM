from django import forms
from issem.models import Departamento, Cid

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ('nome',)

class CidForm(forms.ModelForm):
    class Meta:
        model = Cid
        fields = ('descricao', 'status', 'gravidade')

