# coding:utf-8
from django.db import models


class TipoSanguineoModel(models.Model):
    nome = models.CharField(max_length=128, null=False)

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo Sanguíneo"
        verbose_name_plural = "Tipos Sanguíneos"