# coding:utf-8
from django.shortcuts import HttpResponse
from django.core import serializers
from django.views.generic.base import View
from issem.models import CidadeModel


class CidadeView(View):

    def post(self, request):
        if request.POST['estado']:
            id_estado = request.POST['estado']
            cidades = CidadeModel.objects.filter(uf=id_estado)
            json = serializers.serialize("json", cidades)
            return HttpResponse(json)
        else:
            cidades = CidadeModel.objects.filter(uf=-1)  # PASSA-SE -1 PARA NÃO RETORNAR NENHUM VALOR
            json = serializers.serialize("json", cidades)
            return HttpResponse(json)
