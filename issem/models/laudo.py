# coding: utf-8
from django.db import models
from issem.models import AdendoModel
from issem.models import BeneficioModel
from issem.models import CidModel
from issem.models import ExameModel
from issem.models import ProcedimentoMedicoModel
from issem.models.segurado import SeguradoModel
from issem.models.requerimento import RequerimentoModel
from issem.models.servidor import ServidorModel


class LaudoModel(models.Model):
    data = models.DateField()
    observacoes = models.CharField(max_length=1000)
    segurado = models.ForeignKey(SeguradoModel, null=True, blank=True)
    requerimento = models.ForeignKey(RequerimentoModel, null=False, blank=True)
    medico = models.ForeignKey(ServidorModel, null=True, blank=True)
    historico_doenca = models.CharField(max_length=1000)
    beneficio = models.ForeignKey(BeneficioModel, null=True, blank=True)
    procedimento_medico = models.ManyToManyField(ProcedimentoMedicoModel, blank=True)
    cid = models.ManyToManyField(CidModel, blank=True)
    adendo_laudo = models.ManyToManyField(AdendoModel, blank=True)
    exames_apresentados = models.ManyToManyField(ExameModel, blank=True)
    anamnese = models.CharField(max_length=1000)
    invalidez = models.BooleanField(default=0)
    pericia_revisional = models.BooleanField(default=0)
    incapacidade_doenca_decorre_de_acidente_de_trabalho = models.BooleanField(default=0)
    servidor_readaptado = models.BooleanField(default=0)
    excluido = models.BooleanField(default=False)

    def __unicode__(self):
        return "Laudo de " + str(self.segurado.nome) + " criado em " + str(self.data)

    def __str__(self):
        return "Laudo de " + str(self.segurado.nome) + " criado em " + str(self.data)

    class Meta:
        verbose_name = "Laudo Médico"
        verbose_name_plural = "Laudos Médicos"
