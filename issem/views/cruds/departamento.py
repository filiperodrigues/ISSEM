# coding:utf-8
from django.shortcuts import HttpResponse
from django.core import serializers
from django.views.generic.base import View
from django.contrib.auth.models import Group


class DepartamentoView(View):

    def post(self, request):
        departamento = Group.objects.all().exclude(name='Segurado').exclude(name='Dependente')
        json = serializers.serialize("json", departamento)
        return HttpResponse(json)