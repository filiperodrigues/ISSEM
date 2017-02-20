# coding: utf-8
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'issem_project.settings')

import django

django.setup()

from issem.models import *
from django.contrib.auth.models import Group

def populate():

    # GRUPOS
    grupos = ['Administrativo', 'Técnico', 'Segurado', 'Dependente']
    for g in grupos:
        add_grupo(g)

    # BENEFÍCIOS
    beneficios = [
        [1, "2010-10-10", "2010-10-10", "2010-10-10", "2010-10-10", "Benefício por incapacidade", 1, "2010-10-10", 3.500,
         "Comparecer  ao  ISSEM  munido  de  documento oficial com foto", 5],
        [0, "2010-10-10", "2010-10-10", "2010-10-10", "2010-10-10", "Licença Adoção", 2, "2010-10-10", 4.000,
         "Comparecer  ao  ISSEM  munido  de  documento oficial com foto", 4],
        [1, "2010-10-10", "2010-10-10", "2010-10-10", "2010-10-10", "Prorrogação do benefício por incapacidade", 3, "2010-10-10", 4.500,
         "Comparecer  ao  ISSEM  munido  de  documento oficial com foto", 8],
    ]
    for b in beneficios:
        add_beneficio(b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8], b[9], b[10])

    # CARGOS
    cargos = ['Chefe', 'Secretária', 'Técnico']
    for c in cargos:
        add_cargo(c)

    # TIPOS DE LAUDO
    tipos_laudos = ['Inclusão de Dependente Inválido', 'Concessão de Aposentadoria por Invalidez', 'Laudo de Exame Médico Pericial', 'Laudo de Perícia Revisional']
    for t in tipos_laudos:
        add_tipo_laudo(t)

    # CIDs
    cids = [
        ['Gripe', 1, 1, 5646421],
        ['Aids', 1, 4, 8974564],
        ['Autismo', 0, 4, 213846213],
        ['Retardado', 0, 5, 214564],
    ]
    for cid in cids:
        add_cid(cid[0], cid[1], cid[2], cid[3])

    # CONTATOS ISSEM
    contatos_issem = [
        ['Eduardo Silva', 'Coordenador', 'Tecnologia da Informação', '(47)99999-9999', 'eduardo@ifc-araquari.edu.br'],
        ['Ivo Riegel', 'Coordenador', 'Fábrica de Software', '(47)88888-8888', 'ivo.riegel@ifc-araquari.edu.br'],
        ['Jonas Espíndola', 'Diretor', 'Direção', '(47)77777-7777', 'jonas.espindola@ifc-araquari.edu.br'],
        ['', '', 'Secretaria', '(47)6666-6666', 'secretaria@ifc-araquari.edu.br'],
    ]
    for contato in contatos_issem:
        add_contato_issem(contato[0], contato[1], contato[2], contato[3], contato[4])

    # ESTADOS
    arq = open("estados.txt", "r")
    texto = arq.readlines()
    for linha in texto:
        if linha[-1] == '\n':
            linha = linha[0:-1]
        id_estado = linha.split(',')[0]
        nome_estado = linha.split(',')[1]
        uf_estado = linha.split(',')[2]
        add_estado(id_estado, nome_estado, uf_estado)
    arq.close()

    # CIDADES
    arq = open("cidades.txt", "r")
    texto = arq.readlines()
    for linha in texto:
        if linha[-1] == '\n':
            linha = linha[0:-1]
        id_cidade = linha.split(',')[0]
        nome_cidade = linha.split(',')[1]
        uf_estado = linha.split(',')[2]
        add_cidade(id_cidade, nome_cidade, EstadoModel.objects.filter(pk=uf_estado)[0])
    arq.close()

    # DEPARTAMENTOS
    departamentos = ['Administrativo', 'Recursos Humanos', 'Tecnologia da Informação', 'Contabilidade']
    for d in departamentos:
        add_departamentos(d)

    # TIPOS DE DEPENDENTE
    tipos_dependente = ['Cônjuge', 'Incapaz', 'Pai', 'Mãe', 'Filho(a)', 'Irmão não emancipado']
    for td in tipos_dependente:
        add_tipo_dependente(td)

    # ESTADO CIVIL
    estado_civil = ['Solteiro(a)', 'Casado(a)', 'Divorciado(a)', 'Viúvo(a)', 'Separado(a)', 'Companheiro(a)']
    for ec in estado_civil:
        add_estado_civil(ec)

    # TIPOS SANGUÍNEOS
    tipos_sanguineos = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-']
    for ts in tipos_sanguineos:
        add_tipo_sanguineo(ts)

    # FUNÇÕES
    funcoes = [
        ['Atendente', 'atender'],
        ['Supervisor', 'supervisionar'],
        ['Contador', 'contar']
    ]
    for f in funcoes:
        add_funcao(f[0], f[1])

    # SECRETARIAS
    secretarias = ['Secretaria 1', 'Secretaria 2', 'Secretaria 3']
    for s in secretarias:
        add_secretaria(s)

    # LOCAIS DE TRABALHO
    cidade_1 = CidadeModel.objects.filter()[0]
    cidade_2 = CidadeModel.objects.filter()[1]
    cidade_3 = CidadeModel.objects.filter()[2]
    secretaria_1 = SecretariaModel.objects.filter()[0]
    secretaria_2 = SecretariaModel.objects.filter()[1]
    secretaria_3 = SecretariaModel.objects.filter()[2]
    locais_trabalho = [
        ['Empresa 1', '12345678901234', 'Rua Joaquina', 568, 'Sala 2', 'Aparecida', 89200542, cidade_1, secretaria_2],
        ['Empresa 2', '12345678901235', 'Rua Terezinha', 569, 'Sala 1', 'Boehmerwald', 89200543, cidade_1,
         secretaria_3],
        ['Empresa 3', '12345678901236', 'Rua da Tia Marta', 468, 'Sala 5', 'Carioca', 89200544, cidade_2, secretaria_1],
        ['Empresa 4', '12345678901237', 'Rua Lulinha', 68, 'Sala 20', 'Vila Velha', 89200545, cidade_2, secretaria_3],
        ['Empresa 5', '12345678901238', 'Rua Dilmãe', 58, 'Sala 15', 'Brasília', 89200546, cidade_3, secretaria_2],
        ['Empresa 6', '12345678901239', 'Rua Tiricutico', 500, 'Sala 8', 'Boa Vista', 89200547, cidade_3, secretaria_1],
    ]
    for lt in locais_trabalho:
        add_local_trabalho(lt[0], lt[1], lt[2], lt[3], lt[4], lt[5], lt[6], lt[7], lt[8])

    # PROCEDIMENTOS MÉDICOS
    procedimentos_medicos = [
        [100, 'Procedimento 1', '50.00'],
        [200, 'Procedimento 2', '80.00'],
        [300, 'Procedimento 3', '178.00'],
    ]
    for pm in procedimentos_medicos:
        add_procedimento_medico(pm[0], pm[1], pm[2])

    # TIPOS DE EXAME
    tipos_exame = [
        ['Exame 1', 'Descrição 1'],
        ['Exame 2', 'Descrição 2'],
        ['Exame 3', 'Descrição 3']
    ]
    for te in tipos_exame:
        add_tipo_exame(te[0], te[1])

    # CONSULTA PARÂMETROS
    consulta_parametros = [
        [20, 5, '08:00', 2, 2],
    ]
    for cp in consulta_parametros:
        add_consulta_parametros(cp[0], cp[1], cp[2], cp[3], cp[4])

def add_beneficio(c, di, df, dr, dp, d, np, dpt, sm, obs, ca):
    return BeneficioModel.objects.get_or_create(concessao=c, data_inicial=di, data_final=df, data_retorno=dr,
                                                data_pericia=dp,
                                                descricao=d, numero_portaria=np, data_portaria=dpt, salario_maximo=sm,
                                                observacao=obs, carencia=ca)

def add_grupo(g):
    return Group.objects.get_or_create(name=g)[0]

def add_cargo(n):
    return CargoModel.objects.get_or_create(nome=n)[0]

def add_cid(d, s, g, c):
    return CidModel.objects.get_or_create(descricao=d, status=s, gravidade=g, cod_cid=c)[0]

def add_contato_issem(n, c, d, t, e):
    return ContatoIssemModel.objects.get_or_create(nome=n, cargo=c, departamento=d, telefone=t, email=e)[0]

def add_cidade(id, n, uf):
    return CidadeModel.objects.get_or_create(id=id, nome=n, uf=uf)[0]

def add_estado(id, n, uf):
    return EstadoModel.objects.get_or_create(id=id, nome=n, uf=uf)[0]

def add_departamentos(n):
    return DepartamentoModel.objects.get_or_create(nome=n)[0]

def add_tipo_dependente(n):
    return TipoDependenteModel.objects.get_or_create(descricao=n)

def add_estado_civil(n):
    return EstadoCivilModel.objects.get_or_create(nome=n)

def add_funcao(n, d):
    return FuncaoModel.objects.get_or_create(nome=n, descricao=d)

def add_local_trabalho(n, cnpj, e, ne, c, b, cep, ci, s):
    return LocalTrabalhoModel.objects.get_or_create(nome=n, cnpj=cnpj, endereco=e, numero_endereco=ne, complemento=c,
                                                    bairro=b, cep=cep, cidade=ci, secretaria=s)

def add_procedimento_medico(c, d, v):
    return ProcedimentoMedicoModel.objects.get_or_create(codigo=c, descricao=d, valor=v)

def add_secretaria(n):
    return SecretariaModel.objects.get_or_create(nome=n)

def add_tipo_exame(n, obs):
    return TipoExameModel.objects.get_or_create(nome=n, observacao=obs)

def add_tipo_sanguineo(n):
    return TipoSanguineoModel.objects.get_or_create(nome=n)

def add_tipo_laudo(n):
    return TipoLaudoModel.objects.get_or_create(nome=n)

def add_consulta_parametros(tc, te, ia, lc, ga):
    return ConsultaParametrosModel.objects.get_or_create(tempo_consulta=tc, tempo_espera=te, inicio_atendimento=ia,
                                                         limite_consultas=lc, gap_agendamento=ga)

# Start execution here!
if __name__ == '__main__':
    print ("Starting ISSEM population script...")
    populate()
