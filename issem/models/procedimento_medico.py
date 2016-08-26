# coding:utf-8
from django.db import models


class ProcedimentoMedicoModel(models.Model):
    codigo = models.CharField(max_length=250)
    descricao = models.CharField(max_length=1000)
    porte = models.CharField(max_length=250)
    custo_operacao = models.FloatField(default=0)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Procedimento médico"
        verbose_name_plural = "Procedimento médicos"