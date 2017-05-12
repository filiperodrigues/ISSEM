# coding:utf-8
from django.db import models


class EstadoCivilModel(models.Model):
    nome = models.CharField(max_length=128, null=False)
    excluido = models.BooleanField(default=0)

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Estado civil"
        verbose_name_plural = "Estado Civil"