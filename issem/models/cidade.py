# coding:utf-8
from django.db import models
from issem.models.estado import EstadoModel


class CidadeModel(models.Model):
    nome = models.CharField(max_length=128, null=False)
    uf = models.ForeignKey(EstadoModel)

    def __str__(self):
        return self.nome