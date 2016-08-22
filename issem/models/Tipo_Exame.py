#coding:utf-8
import datetime
from django.db import models

class Tipo_Exame(models.Model):
    nome = models.CharField(max_length=128, null=False)
    observacao = models.TextField()

    class Meta:
        verbose_name = "Tipo Exame"
        verbose_name_plural = "Tipo Exame"