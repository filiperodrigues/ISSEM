from django.db import models

# Create your models here.
class Departamento(models.Model):
    nome = models.CharField(max_length=128)
    def __str__(self):
        return self.nom

    def __unicode__(self):
        return self.nome

class Cid(models.Model):
    descricao = models.CharField(max_length=128)
    status = models.BooleanField(default=0)
    gravidade = models.IntegerField()
    def __str__(self):
        return self.descricao

    def __unicode__(self):
        return self.descricao

