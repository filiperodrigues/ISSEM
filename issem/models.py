#coding:utf-8
import datetime
from django.db import models

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

    class Meta:
        verbose_name = "CID"
        verbose_name_plural = "CIDs"

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
    custo_operacao = models.FloatField(default=0)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Procedimento médico"
        verbose_name_plural = "Procedimentos médicos"

class Beneficio(models.Model):
   concessao = models.BooleanField(default=0)
   data_inicial = models.DateField(default=datetime.date.today)
   data_final = models.DateField(default=datetime.date.today)
   data_retorno = models.DateField(default=datetime.date.today)
   data_pericia = models.DateField(default=datetime.date.today)
   descricao = models.CharField(max_length=1000)
   numero_portaria = models.IntegerField()
   data_portaria = models.DateField(default=datetime.date.today)
   salario_maximo = models.IntegerField()
   observacao = models.CharField(max_length=1000)
   carencia = models.IntegerField()

   def __str__(self):
       return self.descricao

   class Meta:
       verbose_name = "Benefícios"
       verbose_name_plural = "Benefícios"

class Funcao(models.Model):
    nome = models.CharField(max_length=128, null=False)
    descricao = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Função"
        verbose_name_plural = "Funções"

class Cargo(models.Model):
    nome = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.nome

class Tipo_Dependente(models.Model):
    nome = models.CharField(max_length=128, null=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo Dependente"
        verbose_name_plural = "Tipo Dependente"

class Tipo_Exame(models.Model):
    nome = models.CharField(max_length=128, null=False)
    observacao = models.TextField()

    class Meta:
        verbose_name = "Tipo Exame"
        verbose_name_plural = "Tipo Exame"