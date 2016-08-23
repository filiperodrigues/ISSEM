# coding:utf-8
import datetime
from django.db import models
from issem.models.pessoa import Pessoa
from issem.models.departamento import Departamento

class Servidor(Pessoa):
    departamento = models.ForeignKey(Departamento)
    crm = models.IntegerField()

    class Meta:
        verbose_name = 'Servidor'
        verbose_name_plural = 'Servidor'