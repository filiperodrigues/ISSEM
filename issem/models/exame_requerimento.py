# coding:utf-8
from django.db import models
from issem.models.requerimento import RequerimentoModel

class ExameRequerimentoModel(models.Model):
    descricao = models.CharField(max_length=1000)
    arquivo = models.FileField()
    requerimento = models.ForeignKey(RequerimentoModel)

    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Exame Requerimento"
        verbose_name_plural = "Exames Requerimentos"