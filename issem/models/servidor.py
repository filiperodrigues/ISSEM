# coding:utf-8
from django.db import models
from issem.models.pessoa import PessoaModel
from issem.models.funcao import FuncaoModel


class ServidorModel(PessoaModel):
    crm = models.CharField(max_length=32, blank=True)
    funcao = models.ForeignKey(FuncaoModel, null=True, blank=True)
    administrador = models.BooleanField(default=False)

    def __unicode__(self):
        return self.get_full_name()

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = "Servidor"
        verbose_name_plural = "Servidores"