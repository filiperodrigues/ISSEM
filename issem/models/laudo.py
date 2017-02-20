# coding: utf-8
from django.db import models
from issem.models.segurado import SeguradoModel
from issem.models.requerimento import RequerimentoModel
from issem.models.servidor import ServidorModel
from issem.models.tipo_laudo import TipoLaudoModel


class LaudoModel(models.Model):
    tipo_laudo = models.ForeignKey(TipoLaudoModel, null=True, blank=True)
    segurado = models.ForeignKey(SeguradoModel, null=True, blank=True)
    requerimento = models.ForeignKey(RequerimentoModel, null=False, blank=True)
    medico = models.ForeignKey(ServidorModel, null=True, blank=True)
    data = models.DateField()
    observacoes_justificativas = models.CharField(max_length=1000)
    historico_doenca = models.CharField(max_length=1000)


    def __unicode__(self):
        return "Laudo" + str(self.id)

    def __str__(self):
        return "Laudo" + str(self.id)

    class Meta:
        verbose_name = "Laudo"
        verbose_name_plural = "Laudos"
