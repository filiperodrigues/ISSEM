# coding:utf-8
from django.db import models


class Estado(models.Model):
    uf = models.CharField(max_length=2, unique=True, null=False)
    nome = models.CharField(max_length=128, unique=True, null=False)

    def __str__(self):
        return self.nome