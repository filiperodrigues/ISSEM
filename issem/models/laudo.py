# coding: utf-8
from django.db import models
from issem.models.adendo import AdendoModel
from issem.models.beneficio import BeneficioModel
from issem.models.cid import CidModel
from issem.models.exame import ExameModel
from issem.models.procedimento_medico import ProcedimentoMedicoModel
from issem.models.segurado import SeguradoModel
from issem.models.requerimento import RequerimentoModel
from issem.models.servidor import ServidorModel


class LaudoModel(models.Model):
    data = models.DateField()
    observacoes = models.CharField(max_length=1000)
    segurado = models.ForeignKey(SeguradoModel, null=True, blank=True)
    requerimento = models.ForeignKey(RequerimentoModel)
    medico = models.ForeignKey(ServidorModel, null=True, blank=True)
    historico_doenca = models.CharField(max_length=1000)
    beneficio = models.ForeignKey(BeneficioModel, null=True, blank=True)
    procedimento_medico = models.ManyToManyField(ProcedimentoMedicoModel, blank=True)
    cid = models.ManyToManyField(CidModel, blank=True)
    adendo_laudo = models.ManyToManyField(AdendoModel, blank=True)
    exames_apresentados = models.ManyToManyField(ExameModel, blank=True)
    anamnese = models.CharField(max_length=1000)
    invalidez = models.BooleanField(default=False)
    pericia_revisional = models.BooleanField(default=False)
    incapacidade_doenca_decorre_de_acidente_de_trabalho = models.BooleanField(default=False)
    servidor_readaptado = models.BooleanField(default=False)
    excluido = models.BooleanField(default=False)

    def __unicode__(self):
        return "Laudo de " + str(self.segurado.get_full_name()) + " criado em " + str(self.data)

    def __str__(self):
        return "Laudo de " + str(self.segurado.get_full_name()) + " criado em " + str(self.data)

    class Meta:
        verbose_name = "Laudo Médico"
        verbose_name_plural = "Laudos Médicos"
