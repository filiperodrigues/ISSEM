# coding: utf-8
from django.db import models

from issem.models import BeneficioModel
from issem.models import CidModel
from issem.models import ProcedimentoMedicoModel
from issem.models.segurado import SeguradoModel
from issem.models.requerimento import RequerimentoModel
from issem.models.servidor import ServidorModel
from issem.models.tipo_laudo import TipoLaudoModel


class LaudoModel(models.Model):
    data = models.DateField()
    observacoes = models.CharField(max_length=1000)
    tipo_laudo = models.ForeignKey(TipoLaudoModel, null=True, blank=True)
    segurado = models.ForeignKey(SeguradoModel, null=True, blank=True)
    requerimento = models.ForeignKey(RequerimentoModel, null=False, blank=True)
    medico = models.ForeignKey(ServidorModel, null=True, blank=True)
    historico_doenca = models.CharField(max_length=1000)

    # ========= CAMPOS AINDA NÃO CRIADOS, MAS MODELOS JÁ EXISTENTES ========= #

    # beneficio = models.ForeignKey(BeneficioModel, null=True, blank=True)
    # procedimento_medico = models.ForeignKey(ProcedimentoMedicoModel, null=True, blank=True)
    # cid = models.ForeignKey(CidModel, null=True, blank=True)
    # adendo_laudo = models.ForeignKey(AdendoLaudoModel, null=True, blank=True)


    def __unicode__(self):
        return "Laudo" + str(self.id)

    def __str__(self):
        return "Laudo" + str(self.id)

    class Meta:
        verbose_name = "Laudo"
        verbose_name_plural = "Laudos"
