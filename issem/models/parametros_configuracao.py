# coding: utf-8
from django.db import models
# from tinymce import models as tinymce_models
from django.db import models
from tinymce.models import HTMLField

from django.db import models
from tinymce import models as tinymce_models


class ParametrosConfiguracaoModel(models.Model):
    tempo_consulta = models.IntegerField(null=False)
    tempo_espera = models.IntegerField(null=False)
    inicio_atendimento = models.TimeField()
    limite_consultas = models.IntegerField(null=False)
    gap_agendamento = models.IntegerField()
    tempo_minimo_exercicio = models.IntegerField()
    descricao_issem = models.CharField(null=True, blank=True, max_length=500)
    msg_requerimento = models.CharField(null=True, blank=True, max_length=500)



    def __unicode__(self):
        return "Parametro de Configuracao"

    def __str__(self):
        return "Parametro de Configuracao"

    class Meta:
        verbose_name = "Parametro de Configuracao"
        verbose_name_plural = "Parametros de Configuracoes"
