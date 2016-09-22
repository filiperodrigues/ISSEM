# coding:utf-8
import datetime
from django.db import models
from issem.models.tipo_dependente import TipoDependenteModel
from issem.models.pessoa import PessoaModel


class DependenteModel(PessoaModel):
    tipo = models.ForeignKey(TipoDependenteModel)
    data_inicial = models.DateField()
    data_final = models.DateField()

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Dependente"
        verbose_name_plural = "Dependentes"