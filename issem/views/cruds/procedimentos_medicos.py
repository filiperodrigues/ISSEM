# coding:utf-8
from django.shortcuts import HttpResponse
from django.core import serializers
from django.views.generic.base import View
from issem.models.procedimento_medico import ProcedimentoMedicoModel


class BuscaProcedimentosMedicosView(View):
    def post(self, request):
        if request.POST['procedimento_medico'] and request.POST['procedimento_medico'] != " ":
            pesquisa = request.POST['procedimento_medico']
            dados = ProcedimentoMedicoModel.objects.filter(procedimento__icontains=pesquisa)
            json = serializers.serialize("json", dados)
            return HttpResponse(json)
        else:
            dados = ProcedimentoMedicoModel.objects.filter(uf=-1)  # PASSA-SE -1 PARA NÃO RETORNAR NENHUM VALOR
            json = serializers.serialize("json", dados)
            return HttpResponse(json)
