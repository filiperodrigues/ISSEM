# coding: utf-8
from django.db import models


class ConsultaParametrosModel(models.Model):
    tempo_consulta = models.IntegerField(null=False)
    tempo_espera = models.IntegerField(null=False)
    inicio_atendimento = models.TimeField(null=False)
    limite_consultas = models.IntegerField(null=False)
    gep_agendamento = models.CharField(null=False, max_length=8)

    def __unicode__(self):
        return self.tempo_consulta

    def __str__(self):
        return self.tempo_consulta

    class Meta:
        verbose_name = "Consulta Parâmetro"
        verbose_name_plural = "Consulta Parâmetros"
