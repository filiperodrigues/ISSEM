# coding:utf-8
from django.db import models


class TipoDependenteModel(models.Model):
    descricao = models.CharField(max_length=128, null=False)

    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Tipo Dependente"
        verbose_name_plural = "Tipos de Dependente"