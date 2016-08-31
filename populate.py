# coding: utf-8
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'issem_project.settings')

import django
django.setup()

from issem.models import *

def populate():

    # BENEFÍCIOS
    beneficios = [
        [1,"2010-10-10","2010-10-10","2010-10-10","2010-10-10","Benefício 1",1,"2010-10-10",3.500,"Observação 1",5],
        [0,"2010-10-10","2010-10-10","2010-10-10","2010-10-10","Benefício 2",2,"2010-10-10",4.000,"Observação 1",4],
        [1,"2010-10-10","2010-10-10","2010-10-10","2010-10-10","Benefício 3",3,"2010-10-10",4.500,"Observação 1",8],
        [0,"2010-10-10","2010-10-10","2010-10-10","2010-10-10","Benefício 4",4,"2010-10-10",5.000,"Observação 1",2],
        [0,"2010-10-10","2010-10-10","2010-10-10","2010-10-10","Benefício 5",5,"2010-10-10",5.500,"Observação 1",7],
    ]
    for registro in beneficios:
        add_beneficio(concessao=registro[0],data_inicial=registro[1],data_final=registro[2],data_retorno=registro[3],data_pericia=registro[4],
            descricao=registro[5],numero_portaria=registro[6],data_portaria=registro[7],salario_maximo=registro[8],observacao=registro[9],
            carencia=registro[10])

    # CARGOS
    cargos = ['Administrador','Secretária','Chefe','Supervisor']
    for cargo in cargos:
        add_cargo(nome=cargo)

    # CID
    cids = [
        ['Gripe',1,1],
        ['Aids',1,4],
        ['Autismo',0,4],
        ['Retardado',0,5],
    ]
    for cid in cids:
        add_cid(cid[0],cid[1],cid[2])

    # ESTADOS E CIDADES
    estados = {'SC':'Santa Catarina','RS':'Rio Grande do Sul','PR':'Paraná'}
    cidades = [{'Joinville','Florianópolis','Barra do Sul','São Francisco do Sul'},
               {'Pelotas','Porto Alegre','Gramado'},
               {'Curitiba','Morretes','Manoel Ribas'}]
    for i, estado in enumerate(estados.items()):
        estado = add_estado(nome=estado[1],uf=estado[0])
        for cidade in cidades[i]:
            add_cidade(nome=cidade, uf=estado)

def add_beneficio(concessao, data_inicial, data_final, data_retorno, data_pericia, descricao, numero_portaria,
                  data_portaria, salario_maximo, observacao, carencia):
    beneficio = BeneficioModel.objects.get_or_create(concessao=concessao, data_inicial=data_inicial, data_final=data_final,
                    data_retorno=data_retorno, data_pericia=data_pericia, descricao=descricao,numero_portaria=numero_portaria,
                    data_portaria=data_portaria, salario_maximo=salario_maximo,observacao=observacao, carencia=carencia)
    return beneficio

def add_cargo(nome):
    cargo = CargoModel.objects.get_or_create(nome=nome)[0]
    return cargo

def add_cid(descricao,status,gravidade):
    cid = CidModel.objects.get_or_create(descricao=descricao, status=status, gravidade=gravidade)[0]
    return cid

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