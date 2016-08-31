# coding:utf-8
from django.db import models
from issem.models.estado import EstadoModel


class CidadeModel(models.Model):
    nome = models.CharField(max_length=128, null=False)
    uf = models.ForeignKey(EstadoModel)

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"