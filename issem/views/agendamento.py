# coding:utf-8
from datetime import datetime
from django.shortcuts import render, HttpResponseRedirect
from issem.models import AgendamentoModel
from issem.forms import AgendamentoForm
from django.views.generic.base import View
from issem.models.consulta_parametros import ConsultaParametrosModel


class AgendamentoView(View):
    template = 'agendamento.html'

    def get(self, request, id=None):
        if id:
            agendamento = AgendamentoModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = AgendamentoForm(instance=agendamento)
        else:
            form = AgendamentoForm()  # MODO CADASTRO: recebe o formulário vazio
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id})

    def post(self, request):
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            agendamento = AgendamentoModel.objects.get(pk=id)
            form = AgendamentoForm(instance=agendamento, data=request.POST)
        else:  # CADASTRO NOVO
            id = None
            form = AgendamentoForm(data=request.POST)
            tempo_consulta = ConsultaParametrosModel.tempo_consulta
            tempo_espera = ConsultaParametrosModel.tempo_espera
            limite_consultas_diarias = ConsultaParametrosModel.limite_consultas
            gep_agendamento = ConsultaParametrosModel.gep_agendamento

            data_hoje = datetime.today()




        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id})


def AgendamentoDelete(request, id):
    agendamento = AgendamentoModel.objects.get(pk=id)
    agendamento.delete()
    return HttpResponseRedirect('/')
