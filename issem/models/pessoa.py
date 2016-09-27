# coding:utf-8
import datetime
from django.db import models
from issem.models.cidade import CidadeModel
from issem.models.tipo_sanguineo import TipoSanguineoModel
from issem.models.estado_civil import EstadoCivilModel
from issem.models.cargo import CargoModel


class PessoaModel(models.Model):
    nome = models.CharField(max_length=128, null=False)
    cpf = models.CharField(null=False, max_length=14)
    email = models.EmailField(max_length=128, blank=True)
    sexo = models.CharField(max_length=1, blank=True)
    data_nascimento = models.DateField(blank=True)
    rg = models.CharField(null=False, max_length=9)
    telefone_residencial = models.CharField(max_length=12, blank=True)
    telefone_celular = models.CharField(max_length=12, blank=True)
    doador = models.BooleanField(default=0)
    endereco = models.CharField(max_length=128, blank=True)
    numero_endereco = models.PositiveIntegerField(blank=True)
    complemento = models.CharField(max_length=128, blank=True)
    bairro = models.CharField(max_length=128, blank=True)
    cep = models.CharField(null=False, max_length=9)
    estado_civil = models.ForeignKey(EstadoCivilModel)
    tipo_sanguineo = models.ForeignKey(TipoSanguineoModel)
    cargo = models.ForeignKey(CargoModel)
    cidade_atual = models.ForeignKey(CidadeModel, related_name="%(app_label)s_%(class)s_atual")
    cidade_natural = models.ForeignKey(CidadeModel, related_name="%(app_label)s_%(class)s_natural")
    nome_pai = models.CharField(max_length=128, blank=True)
    nome_mae = models.CharField(max_length=128, null=False)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.nome

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"