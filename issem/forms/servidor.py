# coding:utf-8
from issem.forms.pessoa import PessoaForm
from issem.models.servidor import ServidorModel



class ServidorForm(PessoaForm):

    class Meta:
        model = ServidorModel
        fields = '__all__'
        exclude = ('date_joined', 'is_active',)

