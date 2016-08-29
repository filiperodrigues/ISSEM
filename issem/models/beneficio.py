# coding:utf-8
import datetime
from django.db import models


class BeneficioModel(models.Model):
   concessao = models.BooleanField(default=0)
   data_inicial = models.DateField(default=datetime.date.today)
   data_final = models.DateField(default=datetime.date.today)
   data_retorno = models.DateField(default=datetime.date.today)
   data_pericia = models.DateField(default=datetime.date.today)
   descricao = models.CharField(max_length=1000)
   numero_portaria = models.PositiveIntegerField()
   data_portaria = models.DateField(default=datetime.date.today)
   salario_maximo = models.PositiveIntegerField()
   observacao = models.CharField(max_length=1000)
   carencia = models.PositiveIntegerField()

   def __str__(self):
       return self.descricao

   class Meta:
       verbose_name = "Benefício"
       verbose_name_plural = "Benefícios"