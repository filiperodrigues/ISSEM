# coding:utf-8
from django.db import models


class Secretaria(models.Model):
    nome = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.nome