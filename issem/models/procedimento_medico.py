# coding:utf-8
from django.db import models


class ProcedimentoMedicoModel(models.Model):
    codigo = models.CharField(max_length=250, null=False)
    procedimento = models.CharField(max_length=1000, null=False)
    porte = models.CharField(max_length=128, null=False)
    valor = models.CharField(max_length=1000, null=False)
    valor_porte = models.CharField(max_length=1000, blank=True, null=True)
    valor_uco = models.CharField(max_length=1000, blank=True, null=True)
    auxiliares = models.CharField(max_length=1000, blank=True, null=True)
    porte_anestesico = models.CharField(max_length=1000, blank=True, null=True)
    qtd_filme = models.CharField(max_length=1000, blank=True, null=True)
    incidencia = models.CharField(max_length=1000, blank=True, null=True)
    excluido = models.BooleanField(default=False)

    def __unicode__(self):
        return self.procedimento

    def __str__(self):
        return self.procedimento

    class Meta:
        verbose_name = "Procedimento Médico"
        verbose_name_plural = "Procedimentos Médicos"