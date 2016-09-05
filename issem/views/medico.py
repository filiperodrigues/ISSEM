# coding:utf-8
from django.shortcuts import render
from issem.models import *


def PaginaMedicoView(request):
    return render(request, 'medico.html')