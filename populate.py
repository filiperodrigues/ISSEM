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
    cargos = ['Chefe','Secretária','Técnico']
    for cargo in cargos:
        add_cargo(nome=cargo)

    # CIDs
    cids = [
        ['Gripe',1,1],
        ['Aids',1,4],
        ['Autismo',0,4],
        ['Retardado',0,5],
    ]
    for cid in cids:
        add_cid(cid[0],cid[1],cid[2])

    # ESTADOS e CIDADES
    estados = [
        ['SC','Santa Catarina'],
        ['RS','Rio Grande do Sul'],
        ['PR','Paraná']
    ]
    cidades = [
        ['Joinville', 'Florianópolis', 'Barra do Sul', 'São Francisco do Sul'],
        ['Pelotas', 'Porto Alegre', 'Gramado'],
        ['Curitiba', 'Morretes', 'Manoel Ribas']
    ]
    for i, estado in enumerate(estados):
        estado_atual = add_estado(estado[0], estado[1])
        for cidade in cidades[i]:
            add_cidade(nome=cidade, uf=estado_atual)

    # DEPARTAMENTOS
    departamentos = ['Administrativo','Recursos Humanos','Tecnologia da Informação','Contabilidade']
    for departamento in departamentos:
        add_departamentos(departamento)

    # TIPOS DE DEPENDENTE
    tipos_dependente = ['Cônjuge','Incapaz','Pai','Mãe','Filho(a)','Irmão não emancipado']
    for tipo_dependente in tipos_dependente:
        add_tipo_dependente(tipo_dependente)

    # DEPENDENTES
    ##### ENVOLVE A CLASSE PESSOA

    # ESTADO CIVIL
    estado_civil = ['Solteiro(a)','Casado(a)','Divorciado(a)','Viúvo(a)','Separado(a)','Companheiro(a)']
    for estado_civil in estado_civil:
        add_estado_civil(estado_civil)

    # FUNÇÕES
    funcoes = [
        ['Atendente','atender'],
        ['Supervisor','supervisionar'],
        ['Contador','contar']
    ]
    for funcao in funcoes:
        add_funcao(funcao[0], funcao[1])

    # LOCAIS DE TRABALHO
    # locais_trabalho = [
    #     ['Empresa 1','12345678901234','Rua Joquina',568,'Sala 2','Aparecida',89200542,],
    # ]
    # nome
    # cnpj
    # endereco
    # numero_endereco
    # complemento
    # bairro
    # cep
    # cidade
    # PESSOAS
    # PROCIDEMENTOS MÉDICOS
    # SECRETARIAS
    # SEGURADOS
    # SERVIDORES
    # TIPOS DE DEPENDENTE
    # TIPOS DE EXAME
    # TIPOS SANGUÍNEOS

def add_beneficio(concessao, data_inicial, data_final, data_retorno, data_pericia, descricao, numero_portaria,
                  data_portaria, salario_maximo, observacao, carencia):
    return BeneficioModel.objects.get_or_create(concessao=concessao, data_inicial=data_inicial, data_final=data_final,
            data_retorno=data_retorno, data_pericia=data_pericia, descricao=descricao,numero_portaria=numero_portaria,
            data_portaria=data_portaria, salario_maximo=salario_maximo,observacao=observacao, carencia=carencia)

def add_cargo(nome):
    return CargoModel.objects.get_or_create(nome=nome)[0]

def add_cid(descricao,status,gravidade):
    return CidModel.objects.get_or_create(descricao=descricao, status=status, gravidade=gravidade)[0]

def add_cidade(nome, uf):
    return CidadeModel.objects.get_or_create(uf=uf, nome=nome)[0]

def add_estado(nome, uf):
    return EstadoModel.objects.get_or_create(nome=nome, uf=uf)[0]

def add_departamentos(nome):
    return DepartamentoModel.objects.get_or_create(nome=nome)[0]

def add_tipo_dependente(nome):
    return TipoDependenteModel.objects.get_or_create(nome=nome)

def add_dependente():
    return

def add_estado_civil(nome):
    return EstadoCivilModel.objects.get_or_create(nome=nome)

def add_funcao(nome, descricao):
    return FuncaoModel.objects.get_or_create(nome=nome, descricao=descricao)




# Start execution here!
if __name__ == '__main__':
    print "Starting ISSEM population script..."
    populate()