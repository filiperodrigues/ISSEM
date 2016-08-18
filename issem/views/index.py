# coding:utf-8
from django.shortcuts import render
from issem.models import *


def index(request):
    departamentos = Departamento.objects.all()
    cids = Cid.objects.all()
    procedimentos_medicos = Procedimento_Medico.objects.all()
    beneficios = Beneficio.objects.all()
    funcoes = Funcao.objects.all()
    cargos = Cargo.objects.all()
    tipo_dependente = Tipo_Dependente.objects.all()
    tipo_exame = Tipo_Exame.objects.all()
    tipo_sangue = Tipo_Sangue.objects.all()
    estado_civil = Estado_Civil.objects.all()

    context_dict = {'departamentos': departamentos, 'cids': cids, 'procedimentos_medicos': procedimentos_medicos, 'beneficios': beneficios, 'funcoes': funcoes, 'cargos': cargos, 'tipo_dependente': tipo_dependente, 'tipo_exame': tipo_exame, 'tipo_sangue': tipo_sangue, 'estado_civil': estado_civil}
    return render(request, 'index.html', context_dict)