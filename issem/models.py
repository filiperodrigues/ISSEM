import datetime
from django.db import models

# Create your models here.
class Departamento(models.Model):
    nome = models.CharField(max_length=128, unique=True, null=False)

    def __str__(self):
        return self.nome

class Cid(models.Model):
    descricao = models.CharField(max_length=128, null=False)
    status = models.BooleanField(default=0)
    gravidade = models.IntegerField(null=False)
    def __str__(self):
        return self.descricao


class Estado(models.Model):
    uf = models.CharField(max_length=2, unique=True, null=False)
    nome = models.CharField(max_length=128, unique=True, null=False)
    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=128, null=False)
    uf = models.ForeignKey(Estado)
    def __str__(self):
        return self.nome

class Procedimento_Medico(models.Model):
    codigo = models.CharField(max_length=250)
    descricao = models.CharField(max_length=1000)
    porte = models.CharField(max_length=250)
    custo_op = models.FloatField(default=0)
    def __str__(self):
        return  self.codigo

    class Meta:
        verbose_name = "Procedimento Médico"
        verbose_name_plural = "Procedimento Médico"

class Beneficios(models.Model):
   concessao = models.BooleanField(default=0)
   dt_inicial = models.DateField(default=datetime.date.today)
   dt_final = models.DateField(default=datetime.date.today)
   dt_retorno = models.DateField(default=datetime.date.today)
   dt_pericia = models.DateField(default=datetime.date.today)
   descricao = models.CharField(max_length=1000)
   nr_portaria = models.IntegerField()
   dt_portaria = models.DateField(default=datetime.date.today)
   salario_max = models.IntegerField()
   observacao = models.CharField(max_length=1000)
   carencia = models.IntegerField()
   def __str__(self):
       return self.descricao

   def __str__(self):
       return self.observacao

   class Meta:
       verbose_name = "Benefícios"
       verbose_name_plural = "Benefícios"
