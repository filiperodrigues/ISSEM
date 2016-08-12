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