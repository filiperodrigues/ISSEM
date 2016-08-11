from django.db import models

# Create your models here.
class Departamento(models.Model):
    nome_departamento = models.CharField(max_length=128)
    def __str__(self):
        return self.nome_departamento

    def __unicode__(self):
        return self.nome_departamento

class Cid(models.Model):
    descricao_cid = models.CharField(max_length=128)
    status = models.BooleanField(default=0)
    gravidade_cid = models.IntegerField()
    def __str__(self):
        return self.descricao_cid

    def __unicode__(self):
        return self.descricao_cid

