# coding:utf-8
from issem.models.dependente import DependenteModel
from issem.forms.pessoa import PessoaForm


class DependenteForm(PessoaForm):

    class Meta:
        model = DependenteModel
        fields = '__all__'
