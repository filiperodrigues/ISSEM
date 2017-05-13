# coding:utf-8
from django.db import models


class AdendoModel(models.Model):
    descricao = models.CharField(max_length=1000)
    data = models.DateField()

    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Adendo"
        verbose_name_plural = "Adendos"