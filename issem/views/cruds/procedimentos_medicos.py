# coding:utf-8
from django.shortcuts import HttpResponse
from django.core import serializers
from django.views.generic.base import View
from issem.models import ProcedimentoMedicoModel


class BuscaProcedimentosMedicosView(View):

    def post(self, request):
        if request.POST['procedimento_medico']:
            descricao = request.POST['procedimento_medico']
            procedimentos_medicos = ProcedimentoMedicoModel.objects.filter(procedimento=descricao)
            json = serializers.serialize("json", procedimentos_medicos)
            return HttpResponse(json)
        else:
            cidades = ProcedimentoMedicoModel.objects.filter(uf=-1)  # PASSA-SE -1 PARA NÃO RETORNAR NENHUM VALOR
            json = serializers.serialize("json", cidades)
            return HttpResponse(json)
