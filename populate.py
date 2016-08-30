# coding: utf-8
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'issem_project.settings')

import django
django.setup()

from issem.models import *

def populate():

    # ESTADOS E CIDADES

    estados = {'SC':'Santa Catarina','RS':'Rio Grande do Sul','PR':'Paraná'}
    cidades = [{'Joinville','Florianópolis','Barra do Sul','São Francisco do Sul'},
               {'Pelotas','Porto Alegre','Gramado'},
               {'Curitiba','Morretes','Manoel Ribas'}]

    for i, estado in enumerate(estados.items()):
        estado = add_estado(nome=estado[1],uf=estado[0])
        for cidade in cidades[i]:
            add_cidade(nome=cidade, uf=estado)


def add_cidade(nome, uf):
    cidade = CidadeModel.objects.get_or_create(uf=uf, nome=nome)[0]
    return cidade

def add_estado(nome, uf):
    estado = EstadoModel.objects.get_or_create(nome=nome, uf=uf)[0]
    return estado

# Start execution here!
if __name__ == '__main__':
    print "Starting ISSEM population script..."
    populate()