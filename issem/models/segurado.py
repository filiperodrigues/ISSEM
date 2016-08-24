# coding:utf-8
import datetime
from django.db import models
from issem.models.local_trabalho import Local_Trabalho
from issem.models.pessoa import Pessoa
from issem.models.dependente import Dependente

class Segurado(Pessoa):
    pasep_pis_nit = models.IntegerField()
    local_trabalho = models.ForeignKey(Local_Trabalho)
    data_admissao = models.DateField(default=datetime.date.today)
    documento_legal = models.IntegerField()
    dependente = models.ManyToManyField(Dependente)