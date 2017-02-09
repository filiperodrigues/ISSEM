# coding: utf-8
from django.db import models
from issem.models.cargo import CargoModel


class ContatoIssemModel(models.Model):
    nome = models.CharField(max_length=128, blank=True)
    cargo = models.CharField(max_length=128, blank=True)
    departamento = models.CharField(max_length=128, blank=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)

    def __unicode__(self):
        return "Contato ISSEM" + str(self.id)

    def __str__(self):
        return "Contato ISSEM" + str(self.id)

    class Meta:
        verbose_name = "Contato ISSEM"
        verbose_name_plural = "Contatos ISSEM"