from issem.models import BeneficioModel
from django.shortcuts import render

def ApresentaPaginaSegurado(request):
    context_dict = {}
    context_dict['beneficios'] = BeneficioModel.objects.all()
    return render(request, 'segurado_pagina.html', context_dict)