# coding:utf-8
from django.db import models
from issem.models.exame import ExameModel
from issem.models.beneficio import BeneficioModel
from issem.models.segurado import SeguradoModel
from issem.models.servidor import ServidorModel


class RequerimentoModel(models.Model):
    beneficio = models.ForeignKey(BeneficioModel)
    data_requerimento = models.DateField(blank=True)
    servidor = models.ForeignKey(ServidorModel, null=True, blank=True)
    segurado = models.ForeignKey(SeguradoModel)
    data_inicio_afastamento = models.DateField()
    data_final_afastamento = models.DateField()
    possui_agendamento = models.BooleanField(default=False)
    exames = models.ManyToManyField(ExameModel, blank=True)

    def __unicode__(self):
        return str(self.data_requerimento) + " " + str(self.data_requerimento) + " " + str(self.possui_agendamento) + " " + str(self.id)

    def __str__(self):
        return str(self.data_requerimento) + " " + str(self.data_requerimento) + " " + str(self.possui_agendamento) + " " + str(self.id)

    class Meta:
        verbose_name = "Requerimento"
        verbose_name_plural = "Requerimentos"
