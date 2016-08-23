# coding:utf-8
from django.db import models
from issem.models.tipo_dependente import Tipo_Dependente
from issem.models.pessoa import Pessoa

class dependente(Pessoa):
    tipo = models.ForeignKey(Tipo_Dependente)
