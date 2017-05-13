# coding:utf-8
from django.db import models


class ExameModel(models.Model):
    descricao = models.CharField(max_length=1000)
    foto = models.FileField(upload_to='exames')

    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Exame"
        verbose_name_plural = "Exames"