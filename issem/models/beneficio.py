# coding:utf-8
import datetime
from django.db import models


class BeneficioModel(models.Model):
    concessao = models.BooleanField(default=0)
    data_inicial = models.DateField()
    data_final = models.DateField()
    data_retorno = models.DateField()
    data_pericia = models.DateField()
    descricao = models.CharField(max_length=1000)
    numero_portaria = models.PositiveIntegerField()
    data_portaria = models.DateField()
    salario_maximo = models.PositiveIntegerField()
    observacao = models.CharField(max_length=1000)
    carencia = models.PositiveIntegerField()

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Benefício"
        verbose_name_plural = "Benefícios"