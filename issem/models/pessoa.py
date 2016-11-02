# coding:utf-8
import datetime
from django.db import models
from issem.models.cidade import CidadeModel
from issem.models.tipo_sanguineo import TipoSanguineoModel
from issem.models.estado_civil import EstadoCivilModel
from issem.models.cargo import CargoModel
from django.contrib.auth.models import User

class PessoaModel(User):
    nome = models.CharField(max_length=128, null=False)
    cpf = models.CharField(null=False, max_length=14)
    sexo = models.CharField(max_length=1, blank=True)
    data_nascimento = models.DateField(blank=True)
    rg = models.CharField(null=False, max_length=9)
    telefone_residencial = models.CharField(max_length=15, blank=True)
    telefone_celular = models.CharField(max_length=15, blank=True)
    doador = models.BooleanField(default=0)
    endereco = models.CharField(max_length=128, blank=True)
    numero_endereco = models.CharField(blank=True, max_length=9)
    complemento = models.CharField(max_length=128, blank=True)
    bairro = models.CharField(max_length=128, blank=True)
    cep = models.CharField(max_length=9, blank=True)
    estado_civil = models.ForeignKey(EstadoCivilModel, null=True, blank=True)
    tipo_sanguineo = models.ForeignKey(TipoSanguineoModel, null=True, blank=True)
    cargo = models.ForeignKey(CargoModel, null=True, blank=True)
    cidade_atual = models.ForeignKey(CidadeModel, related_name="%(app_label)s_%(class)s_atual", null=True, blank=True)
    cidade_natural = models.ForeignKey(CidadeModel, related_name="%(app_label)s_%(class)s_natural", null=True, blank=True)
    nome_pai = models.CharField(max_length=128, blank=True)
    nome_mae = models.CharField(max_length=128, null=False)

    class Meta:
        abstract = True
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"


