# coding:utf-8
from django.db import models
from issem.models.pessoa import PessoaModel
from issem.models.tipo_dependente import TipoDependenteModel


class DependenteModel(PessoaModel):
    tipo = models.ForeignKey(TipoDependenteModel, null=False, blank=False)
    data_inicial = models.DateField(null=True, blank=True)
    data_final = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.get_full_name()

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = "Dependente"
        verbose_name_plural = "Dependentes"