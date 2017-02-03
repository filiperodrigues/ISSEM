# coding: utf-8
from django.db import models
from issem.models.cargo import CargoModel


class ContatoIssemModel(models.Model):
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    descricao = models.CharField(max_length=128)
    cargo = models.ForeignKey(CargoModel, null=True, blank=True)

    def __unicode__(self):
        return "Contato ISSEM" + str(self.id)

    def __str__(self):
        return "Contato ISSEM" + str(self.id)

    class Meta:
        verbose_name = "Contato ISSEM"
        verbose_name_plural = "Contatos ISSEM"