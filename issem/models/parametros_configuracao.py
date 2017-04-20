# coding: utf-8
from django.db import models


class ParametrosConfiguracaoModel(models.Model):
    tempo_consulta = models.IntegerField(null=False)
    tempo_espera = models.IntegerField(null=False)
    inicio_atendimento = models.TimeField()
    limite_consultas = models.IntegerField(null=False)
    gap_agendamento = models.IntegerField()
    tempo_minimo_exercicio = models.IntegerField()

    def __unicode__(self):
        return "Parâmetro de Configuração"

    def __str__(self):
        return "Parâmetro de Configuração"

    class Meta:
        verbose_name = "Parâmetro de Configuração"
        verbose_name_plural = "Parâmetros de Configuração"
