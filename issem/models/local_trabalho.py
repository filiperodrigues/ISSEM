# coding:utf-8
from django.db import models
from issem.models.cidade import CidadeModel


class LocalTrabalhoModel(models.Model):
    nome = models.CharField(max_length=128, null=False)
    cnpj = models.PositiveIntegerField(unique=True)
    endereco = models.CharField(max_length=128)
    numero_endereco = models.PositiveIntegerField()
    complemento = models.CharField(max_length=128)
    bairro = models.CharField(max_length=128)
    cep = models.PositiveIntegerField()
    cidade = models.ForeignKey(CidadeModel)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Local de Trabalho"
        verbose_name_plural = "Locais de Trabalho"