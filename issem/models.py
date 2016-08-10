from django.db import models

# Create your models here.
class Departamento(models.Model):
    nome_departamento = models.CharField(max_length=128)
    def __str__(self):
        return self.nome_departamento

    def __unicode__(self):
        return self.nome_departamento
