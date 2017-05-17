# coding:utf-8
from django.db import models
from issem.models.tipo_dependente import TipoDependenteModel
from issem.models.pessoa import PessoaModel


class DependenteModel(PessoaModel):
    tipo = models.ForeignKey(TipoDependenteModel, null=True, blank=True)
    data_inicial = models.DateField(null=True, blank=True)
    data_final = models.DateField(null=True, blank=True)

    def __unicode__(self):
        nome = str(self.nome) + " " + str(self.id)
        return nome

    def __str__(self):
        nome = str(self.nome) + " " + str(self.id)
        return nome

    class Meta:
        verbose_name = "Dependente"
        verbose_name_plural = "Dependentes"