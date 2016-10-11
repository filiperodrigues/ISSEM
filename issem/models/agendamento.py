# coding:utf-8
from django.db import models
from issem.models.segurado import SeguradoModel
from issem.models.requerimento import RequerimentoModel
from issem.models.servidor import ServidorModel

class AgendamentoModel(models.Model):
    data_agendamento = models.DateField(null=False)
    data_pericia = models.DateField()
    servidor = models.ForeignKey(ServidorModel)
    segurado = models.ForeignKey(SeguradoModel)
    requerimento = models.ForeignKey(RequerimentoModel)

    def __unicode__(self):
        return self.data_agendamento

    def __str__(self):
        return self.data_agendamento

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"
