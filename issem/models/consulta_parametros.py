# coding: utf-8
from django.db import models
import timedelta


class ConsultaParametrosModel(models.Model):
    tempo_consulta = models.IntegerField(null=False)
    tempo_espera = models.IntegerField(null=False)
    inicio_atendimento = models.TimeField()
    limite_consultas = models.IntegerField(null=False)
    gap_agendamento = models.IntegerField()

    def __unicode__(self):
        return "Parâmetro de consulta" + str(self.id)

    def __str__(self):
        return "Parâmetro de consulta" + str(self.id)

    class Meta:
        verbose_name = "Consulta Parâmetro"
        verbose_name_plural = "Consulta Parâmetros"
