# coding:utf-8
import datetime
from django.db import models


class Departamento(models.Model):
    nome = models.CharField(max_length=128, unique=True, null=False)

    def __str__(self):
        return self.nome
