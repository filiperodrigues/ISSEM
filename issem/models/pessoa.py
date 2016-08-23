# coding:utf-8
import datetime
from django.db import models
from issem.models.cidade import Cidade
from issem.models.tipo_sangue import Tipo_Sangue
from issem.models.estado_civil import Estado_Civil
from issem.models.cargo import Cargo


class Pessoa(models.Model):
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
    estado_civil = models.ForeignKey(Estado_Civil)
    tipo_saguineo = models.ForeignKey(Tipo_Sangue)
    cargo = models.ForeignKey(Cargo)
    cidade_natural = models.ForeignKey(Cidade, related_name='cidade_natural')
    cidade_atual = models.ForeignKey(Cidade, related_name='cidade_atual')
