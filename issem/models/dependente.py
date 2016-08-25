# coding:utf-8
import datetime
from django.db import models
from issem.models.tipo_dependente import Tipo_Dependente
from issem.models.pessoa import Pessoa

class Dependente(Pessoa):
    tipo = models.ForeignKey(Tipo_Dependente)
    data_inicio = models.DateField(default=datetime.date.today)
    dat_fim = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.nome