#coding:utf-8
from issem.models.segurado import SeguradoModel
from issem.forms.pessoa import PessoaForm


class SeguradoForm(PessoaForm):

    class Meta:
        model = SeguradoModel
        fields = '__all__'