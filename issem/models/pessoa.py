# coding:utf-8
import datetime
from django.db import models
from issem.models.cidade import CidadeModel
from issem.models.tipo_sangue import TipoSangueModel
from issem.models.estado_civil import EstadoCivilModel
from issem.models.cargo import CargoModel


class PessoaModel(models.Model):
    nome = models.CharField(max_length=128, null=False)
    cpf = models.PositiveIntegerField(null=False)
    email = models.EmailField(max_length=128)
    sexo = models.CharField(max_length=1)
    data_nascimento = models.DateField(default=datetime.date.today)
    rg = models.PositiveIntegerField(null=False)
    telefone_residencial = models.PositiveIntegerField()
    telefone_celular = models.PositiveIntegerField()
    doador = models.BooleanField(default=0)
    endereco = models.CharField(max_length=128)
    numero_endereco = models.PositiveIntegerField()
    complemento = models.CharField(max_length=128)
    bairro = models.CharField(max_length=128)
    cep = models.PositiveIntegerField()
    estado_civil = models.ForeignKey(EstadoCivilModel)
    tipo_saguineo = models.ForeignKey(TipoSangueModel)
    cargo = models.ForeignKey(CargoModel)
    cidade_atual = models.ForeignKey(CidadeModel, related_name="%(app_label)s_%(class)s_atual")
    cidade_natural = models.ForeignKey(CidadeModel, related_name="%(app_label)s_%(class)s_natural")
    nome_pai = models.CharField(max_length=128)
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