# coding: utf-8
from django.db import models


class ConsultaParametrosModel(models.Model):
    tempo_consulta = models.IntegerField(null=False)
    tempo_espera = models.IntegerField(null=False)
    inicio_atendimento = models.TimeField(null=False)
    limite_consultas = models.IntegerField(null=False)

    def __unicode__(self):
        return self.tempo_consulta

    def __str__(self):
        return self.tempo_consulta

    class Meta:
        verbose_name = "Consulta Parâmetro"
        verbose_name_plural = "Consulta Parâmetros"
