# coding:utf-8
from django.db import models


class TipoExameModel(models.Model):
    nome = models.CharField(max_length=128, null=False)
    observacao = models.TextField()

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo de Exame"
        verbose_name_plural = "Tipos de Exame"