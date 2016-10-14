# coding:utf-8
from django.db import models
from issem.models.segurado import SeguradoModel
from issem.models.requerimento import RequerimentoModel
from issem.models.servidor import ServidorModel
from issem.models.cargo import CargoModel
from issem.models.secretaria import SecretariaModel
from issem.models.local_trabalho import LocalTrabalhoModel

class AgendamentoModel(models.Model):
    data_agendamento = models.DateField(null=False)
    data_pericia = models.DateField()
    servidor = models.ForeignKey(ServidorModel)
    segurado = models.ForeignKey(SeguradoModel)
    requerimento = models.ForeignKey(RequerimentoModel)
    cargo = models.ForeignKey(CargoModel)
    secretaria = models.ForeignKey(SecretariaModel)
    local_trabalho = models.ForeignKey(LocalTrabalhoModel)
    data_inicio_afastamento = models.DateField()
    data_final_afastamento = models.DateField()

    def __unicode__(self):
        return self.data_agendamento

    def __str__(self):
        return self.data_agendamento

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"
