# coding:utf-8
from django.db import models


class DepartamentoModel(models.Model):
    nome = models.CharField(max_length=128, unique=True, null=False)

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"