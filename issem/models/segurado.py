# coding:utf-8
from django.db import models
from issem.models.pessoa import PessoaModel
from issem.models.dependente import DependenteModel
from issem.models.funcao import FuncaoModel
from issem.models.local_trabalho import LocalTrabalhoModel


class SeguradoModel(PessoaModel):
    pasep_pis_nit = models.CharField(blank=True, max_length=15)
    local_trabalho = models.ForeignKey(LocalTrabalhoModel, null=True)
    data_admissao = models.DateField()
    documento_legal = models.CharField(blank=True, max_length=15)
    dependente = models.ManyToManyField(DependenteModel, blank=True)
    funcao = models.ForeignKey(FuncaoModel, null=True, blank=True)
    primeiro_login = models.BooleanField(default=True)

    def __unicode__(self):
        return self.get_full_name()

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = "Segurado"
        verbose_name_plural = "Segurados"