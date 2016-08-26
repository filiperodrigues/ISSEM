# coding:utf-8
import datetime
from django.db import models
from issem.models.tipo_dependente import TipoDependenteModel
from issem.models.pessoa import PessoaModel

class DependenteModel(PessoaModel):
    tipo = models.ForeignKey(TipoDependenteModel)
    data_inicio = models.DateField(default=datetime.date.today)
    data_fim = models.DateField(default=datetime.date.today)
    dat_fim = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.nome