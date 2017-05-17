# coding:utf-8
from django.db import models
from issem.models.tipo_exame import TipoExameModel


class ExameModel(models.Model):
    descricao = models.CharField(max_length=1000)
    arquivo = models.FileField(upload_to='exames')
    tipo_exame = models.ForeignKey(TipoExameModel, null=True, blank=True)
    excluido = models.BooleanField(default=False)

    def __unicode__(self):
        return self.descricao

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Exame"
        verbose_name_plural = "Exames"