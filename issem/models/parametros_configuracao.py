# coding: utf-8
from django.db import models


class ParametrosConfiguracaoModel(models.Model):
    tempo_consulta = models.IntegerField(null=False)
    tempo_espera = models.IntegerField(null=False)
    inicio_atendimento = models.TimeField()
    limite_consultas = models.IntegerField(null=False)
    gap_agendamento = models.IntegerField()
    tempo_minimo_exercicio = models.IntegerField()
    descricao_issem = models.TextField(blank=True)


    def __unicode__(self):
        return "Parametro de Configuracao"

    def __str__(self):
        return "Parametro de Configuracao"

    class Meta:
        verbose_name = "Parametro de Configuracao"
        verbose_name_plural = "Parametros de Configuracoes"
