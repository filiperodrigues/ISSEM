# coding:utf-8
from django.db import models
from issem.models.beneficio import BeneficioModel
from issem.models.segurado import SeguradoModel
from issem.models.servidor import ServidorModel


class RequerimentoModel(models.Model):
    beneficio = models.ForeignKey(BeneficioModel)
    data_requerimento = models.DateField(blank=True)
    servidor = models.ForeignKey(ServidorModel, null=True, blank=True)
    segurado = models.ForeignKey(SeguradoModel, null=True, blank=True)
    data_inicio_afastamento = models.DateField()
    data_final_afastamento = models.DateField()
    possui_agendamento = models.BooleanField(default=0)

    def __unicode__(self):
        nome = str(self.segurado.nome) + " " + str(self.data_requerimento)
        return nome

    def __str__(self):
        nome = str(self.segurado.nome) + " " + str(self.data_requerimento)
        return nome

    class Meta:
        verbose_name = "Requerimento"
        verbose_name_plural = "Requerimentos"


