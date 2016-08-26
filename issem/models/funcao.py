# coding:utf-8
from django.db import models


class FuncaoModel(models.Model):
    nome = models.CharField(max_length=128, null=False)
    descricao = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Função"
        verbose_name_plural = "Funções"