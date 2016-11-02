# coding:utf-8
from issem.forms.pessoa import PessoaForm
from issem.models.servidor import ServidorModel



class ServidorForm(PessoaForm):

    class Meta:
        model = ServidorModel
        exclude = ('date_joined', 'is_active',)

