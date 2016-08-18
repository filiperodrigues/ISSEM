# coding:utf-8
from django.db import models
from issem.models import Estado


class Cidade(models.Model):
    nome = models.CharField(max_length=128, null=False)
    uf = models.ForeignKey(Estado)

    def __str__(self):
        return self.nome