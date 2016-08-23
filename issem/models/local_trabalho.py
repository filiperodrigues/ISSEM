# coding:utf-8
from django.db import models
from issem.models.cidade import Cidade


class Local_Trabalho(models.Model):
    nome = models.CharField(max_length=128, null=False)
    cnpj = models.IntegerField(unique=True)
    endereco = models.CharField(max_length=128)
    numero_endereco = models.IntegerField()
    complemento = models.CharField(max_length=128)
    bairro = models.CharField(max_length=128)
    cep = models.IntegerField()
    cidade = models.ForeignKey(Cidade)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Local de Trabalho"
        verbose_name_plural = "Locais de Trabalho"