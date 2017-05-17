# coding:utf-8
from django.db import models
from issem.models.funcao import FuncaoModel
from issem.models.pessoa import PessoaModel


class ServidorModel(PessoaModel):
    crm = models.CharField(max_length=32, blank=True)
    funcao = models.ForeignKey(FuncaoModel, blank=True)

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Servidor"
        verbose_name_plural = "Servidores"