# coding:utf-8
from django.db import models
from issem.models.beneficio import BeneficioModel

class RequerimentoModel(models.Model):
    beneficico = models.ForeignKey(BeneficioModel)
    data_requerimento = models.DateField()

    def __unicode__(self):
        return self.beneficico

    def __str__(self):
        return self.beneficico

    class Meta:
        verbose_name = "Requerimento"
        verbose_name_plural = "Requerimentos"


