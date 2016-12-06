# coding:utf-8
from django.shortcuts import render
from issem.models import *


def index(request):

    grupos = request.user.groups.all()

    if len(grupos) == 0:
        return render(request, 'index.html')

    grupo = str(grupos[0])

    context_dict = {}

    if grupo == "Médico":
        template = 'medico_pagina.html'
    elif grupo == 'Segurado':
        template = 'segurado_pagina.html'
    else:
        context_dict['requerimentos'] = RequerimentoModel.objects.filter(possui_agendamento=False)
        template = 'funcionario_pagina.html'

    return render(request, template, context_dict)
