# coding:utf-8
from django.shortcuts import render
from issem.models import *


def PaginaFuncionarioView(request):
    return render(request, 'funcionario_pagina.html')