# coding:utf-8
from issem.models.servidor import ServidorModel
from issem.forms.pessoa import PessoaForm


class ServidorForm(PessoaForm):

    class Meta:
        model = ServidorModel
        fields = '__all__'