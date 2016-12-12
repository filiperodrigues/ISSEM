# coding:utf-8
from django.db import models


class CidModel(models.Model):
    descricao = models.CharField(max_length=128, null=False)
    status = models.BooleanField(default=0)
    gravidade = models.BooleanField(default=0)
    cod_cid = models.CharField(max_length=128)

    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "CID"
        verbose_name_plural = "CIDs"