# coding:utf-8
from django.db import models


class ProcedimentoMedicoModel(models.Model):
    codigo = models.CharField(max_length=250)
    descricao = models.CharField(max_length=1000)
    valor = models.CharField(max_length=128)
    excluido = models.BooleanField(default=False)

    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Procedimento Médico"
        verbose_name_plural = "Procedimentos Médicos"