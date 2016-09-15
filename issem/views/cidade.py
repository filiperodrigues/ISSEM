# coding:utf-8
from django.shortcuts import HttpResponse
from django.core import serializers
from django.views.generic.base import View
from issem.models import CidadeModel


class CidadeView(View):

    def post(self, request):
        if 'estado' in request.POST:
            id_estado = request.POST['estado']
            cidades = CidadeModel.objects.filter(uf=id_estado)
            json = serializers.serialize("json", cidades)
            return HttpResponse(json)