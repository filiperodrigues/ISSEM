# coding:utf-8
from django.db import models


class EstadoModel(models.Model):
    uf = models.CharField(max_length=2, unique=True, null=False)
    nome = models.CharField(max_length=128, unique=True, null=False)

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"