# coding:utf-8
import datetime
from django.db import models
from issem.models.cidade import CidadeModel
from issem.models.tipo_sangue import TipoSangueModel
from issem.models.estado_civil import EstadoCivilModel
from issem.models.cargo import CargoModel


class PessoaModel(models.Model):
    class Meta:
        abstract = True
    nome = models.CharField(max_length=128, null=False)
    cpf = models.IntegerField(null=False)
    email = models.EmailField(max_length=128)
    sexo = models.CharField(max_length=1)
    data_nascimento = models.DateField(default=datetime.date.today)
    rg = models.IntegerField(null=False)
    telefone_residencial = models.IntegerField()
    telefone_celular = models.IntegerField()
    doador = models.BooleanField(default=0)
    endereco = models.CharField(max_length=128)
    numero_endereco = models.IntegerField()
    complemento = models.CharField(max_length=128)
    bairro = models.CharField(max_length=128)
    cep = models.IntegerField()
    estado_civil = models.ForeignKey(EstadoCivilModel)
    tipo_saguineo = models.ForeignKey(TipoSangueModel)
    cargo = models.ForeignKey(CargoModel)
    cidade_atual = models.ForeignKey(CidadeModel, related_name="%(app_label)s_%(class)s_atual")
    cidade_natural = models.ForeignKey(CidadeModel, related_name="%(app_label)s_%(class)s_natural")
