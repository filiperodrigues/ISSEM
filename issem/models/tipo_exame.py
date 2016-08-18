# coding:utf-8
from django.db import models


class Tipo_Exame(models.Model):
    nome = models.CharField(max_length=128, null=False)
    observacao = models.TextField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo Exame"
        verbose_name_plural = "Tipo Exame"