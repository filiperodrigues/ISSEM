# coding:utf-8
from django.db import models


class TipoDependenteModel(models.Model):
    nome = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo Dependente"
        verbose_name_plural = "Tipos de Dependente"