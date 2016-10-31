# coding:utf-8
from django.db import models
from issem.models.pessoa import PessoaModel
from issem.models.departamento import DepartamentoModel


class ServidorModel(PessoaModel):
    departamento = models.ForeignKey(DepartamentoModel, null=True, blank=True)
    crm = models.CharField(max_length=32, blank=True)

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Servidor"
        verbose_name_plural = "Servidores"