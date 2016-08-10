from django import forms
from issem.models import Departamento, Cid

class DepartamentoForm(forms.ModelForm):
    nome_departamento = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Departamento
        fields = ('nome_departamento',)

class CidForm(forms.ModelForm):
    descricao = forms.CharField(widget=forms.TextInput())
    status = forms.BooleanField()
    gravidade_cid = forms.IntegerField()

    class Meta:
        model = Cid
        fields = ('descricao', 'status', 'gravidade_cid')