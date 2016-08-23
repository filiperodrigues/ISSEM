# coding:utf-8
from django.shortcuts import render
from issem.models import *


def index(request):
    context_dict = {}
    context_dict['departamentos'] = Departamento.objects.all()
    context_dict['cids'] = Cid.objects.all()
    context_dict['procedimentos_medicos'] = Procedimento_Medico.objects.all()
    context_dict['beneficios'] = Beneficio.objects.all()
    context_dict['funcoes'] = Funcao.objects.all()
    context_dict['cargos'] = Cargo.objects.all()
    context_dict['tipo_dependente'] = Tipo_Dependente.objects.all()
    context_dict['tipo_exame'] = Tipo_Exame.objects.all()
    context_dict['tipo_sangue'] = Tipo_Sangue.objects.all()
    context_dict['estado_civil'] = Estado_Civil.objects.all()
    context_dict['secretaria'] = Secretaria.objects.all()
    context_dict['local_trabalho'] = Local_Trabalho.objects.all()

    return render(request, 'index.html', context_dict)