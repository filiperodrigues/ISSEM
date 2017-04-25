# coding:utf-8
import datetime
from django.db import models
from issem.models.local_trabalho import LocalTrabalhoModel
from issem.models.pessoa import PessoaModel
from issem.models.dependente import DependenteModel


class SeguradoModel(PessoaModel):
    pasep_pis_nit = models.CharField(blank=True, max_length=128)
    local_trabalho = models.ForeignKey(LocalTrabalhoModel, null=True)
    data_admissao = models.DateField()
    documento_legal = models.CharField(blank=True, max_length=128)
    dependente = models.ManyToManyField(DependenteModel, blank=True)

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Segurado"
        verbose_name_plural = "Segurados"