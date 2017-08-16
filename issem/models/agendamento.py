# coding:utf-8
from django.db import models
from issem.models.requerimento import RequerimentoModel
from datetime import datetime


class AgendamentoModel(models.Model):
    data_agendamento = models.DateField(blank=True, null=True)
    data_pericia = models.DateField(blank=True, null=True)
    hora_pericia = models.TimeField()
    requerimento = models.ForeignKey(RequerimentoModel, null=True, blank=True)

    def __unicode__(self):
        return str(datetime.combine(self.data_pericia, self.hora_pericia)) +str(" ID Requerimento:") + str(self.requerimento.id)

    def __str__(self):
        return str(datetime.combine(self.data_pericia, self.hora_pericia)) +str(" ID Requerimento:") + str(self.requerimento.id)

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"
