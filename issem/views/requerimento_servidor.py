# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import RequerimentoModel, AgendamentoModel, ConsultaParametrosModel, BeneficioModel
from issem.forms import RequerimentoForm, AgendamentoForm
from django.views.generic.base import View
from datetime import date, datetime
from django.contrib.auth.models import User


class RequerimentoServidorView(View):
    template = 'requerimento_servidor.html'

    def get(self, request, id_requerimento=None, id_beneficio=None, id_agendamento=None):
        usuario_logado = User.objects.get(pk=request.user.id)
        id_usuario = usuario_logado.id
        if id_beneficio:
            beneficio = BeneficioModel.objects.get(pk=id_beneficio)
            beneficio_descricao = beneficio.descricao
            beneficio_id = beneficio.id
        else:
            beneficio_descricao = ""
            beneficio_id = ""

        if id_requerimento:
            requerimento = RequerimentoModel.objects.get(
                pk=id_requerimento)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            agendamento = AgendamentoModel.objects.get(pk=id_agendamento)
            beneficio_id = requerimento.beneficio.id
            beneficio_descricao = requerimento.beneficio.descricao
            form_requerimento = RequerimentoForm(instance=requerimento)
            form_agendamento = AgendamentoForm(instance=agendamento)
        else:
            form_requerimento = RequerimentoForm()  # MODO CADASTRO: recebe o formulário vazio]
            form_agendamento = AgendamentoForm()

        return render(request, self.template,
                      {'form_requerimento': form_requerimento, 'form_agendamento': form_agendamento,
                       'method': 'get', 'id': id_requerimento, 'beneficio_descricao': beneficio_descricao,
                       'id_beneficio': beneficio_id, 'id_agendamento': id_agendamento, 'id_usuario' : id_usuario})

    def post(self, request, id_beneficio=None):
        print("aqui post")
        beneficio = BeneficioModel.objects.get(pk=id_beneficio)
        usuario_logado = User.objects.get(pk=request.user.id)
        id_usuario = usuario_logado.id
        if request.POST['id']:
            id_requerimento = request.POST['id']
            id_agendamento = request.POST['id_agendamento']
            requerimento = RequerimentoModel.objects.get(pk=id_requerimento)
            agendamento = AgendamentoModel.objects.get(pk=id_agendamento)
            form_requerimento = RequerimentoForm(instance=requerimento, data=request.POST)
            form_agendamento = AgendamentoForm(instance=agendamento, data=request.POST)
        else:  # CADASTRO NOVO
            form_requerimento = RequerimentoForm(data=request.POST)
            form_agendamento = AgendamentoForm(data=request.POST)

        print(form_requerimento)
        if form_requerimento.is_valid():
            current_user = request.user
            form_requerimento.segurado = current_user
            form_requerimento.servidor = current_user
            obj = form_requerimento.save(commit=False)
            obj.possui_agendamento = True
            obj.save()
            form_requerimento.save()

            requerimento = RequerimentoModel.objects.latest('id')
            id = requerimento.id

            if request.POST['id_agendamento']:
                obj = form_agendamento.save(commit=False)
                obj.requerimento_id = id_requerimento
                obj.data_agendamento = date.today()
                obj.save()

            else:
                form_agendamento_model = AgendamentoModel()
                form_agendamento_model.requerimento_id = id
                form_agendamento_model.data_agendamento = date.today()
                data_pericia = form_agendamento._raw_value('data_pericia')
                data_pericia = data_pericia.split('/')
                form_agendamento_model.data_pericia = datetime(int(data_pericia[2]), int(data_pericia[1]),
                                                               int(data_pericia[0]))
                form_agendamento_model.hora_pericia = form_agendamento._raw_value('hora_pericia')

                form_agendamento_model.save()

            msg = "Consulta agendada"
            return render(request, self.template, {'msg': msg, 'beneficio_descricao': beneficio.descricao, 'id_usuario' : id_usuario})

        else:
            print('deu um pouco de ruim')
            print(form_requerimento.errors)

        return render(request, self.template,
                      {'form_requerimento': form_requerimento, 'form_agendamento': form_agendamento,
                       'method': 'post', 'id_beneficio': id_beneficio, 'id_usuario' : id_usuario})


def RequerimentoDelete(request, id):
    requerimento = RequerimentoModel.objects.get(pk=id)
    requerimento.delete()
    return HttpResponseRedirect('/')


def ApresentaAgendamentos(request):
    context_dict = {}
    context_dict['agendamentos'] = AgendamentoModel.objects.all().order_by('data_pericia')
    return render(request, 'tabela_agendamentos.html', context_dict)
