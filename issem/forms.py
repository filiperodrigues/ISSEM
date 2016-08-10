from django import forms
from issem.models import Departamento

class DepartamentoForm(forms.ModelForm):
    nome_departamento = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Departamento
        fields = ('nome_departamento',)
