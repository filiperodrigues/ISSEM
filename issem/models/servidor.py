# coding:utf-8
from django.db import models
from issem.models.pessoa import PessoaModel
from issem.models.departamento import DepartamentoModel

class ServidorModel(PessoaModel):
    departamento = models.ForeignKey(DepartamentoModel)
    crm = models.PositiveIntegerField()
