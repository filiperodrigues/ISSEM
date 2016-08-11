import datetime
from django.db import models

# Create your models here.
class Departamento(models.Model):
    nome_departamento = models.CharField(max_length=128)
    def __str__(self):
        return self.nome_departamento

    def __unicode__(self):
        return self.nome_departamento

class Cid(models.Model):
    descricao_cid = models.CharField(max_length=128)
    status = models.BooleanField(default=0)
    gravidade_cid = models.IntegerField()
    def __str__(self):
        return self.descricao_cid

    def __unicode__(self):
        return self.descricao_cid

class Beneficios(models.Model):
   concessao = models.BooleanField(default=0)
   dt_inicial = models.DateField(initial=datetime.date.today)
   dt_final = models.DateField(initial=datetime.date.today)
   dt_retorno = models.DateField(initial=datetime.date.today)
   dt_pericia = models.DateField(initial=datetime.date.today)
   descricao = models.CharField(max_length=1000)
   nr_portaria = models.IntegerField()
   dt_portaria = models.DateField(initial=datetime.date.today)
   max_salario = models.IntegerField()
   observacao = models.CharField(max_length=1000)
   carencia = models.IntegerField()


