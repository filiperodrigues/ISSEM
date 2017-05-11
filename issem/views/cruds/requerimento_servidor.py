# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import RequerimentoModel, AgendamentoModel, ParametrosConfiguracaoModel, BeneficioModel
from issem.forms import RequerimentoForm, AgendamentoForm, FiltroAgendaForm
from django.views.generic.base import View
from datetime import date, datetime
from django.contrib.auth.models import User
from issem.views.pagination import pagination


class RequerimentoServidorView(View):
    template = 'cruds/requerimento_servidor.html'

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
            requerimento = RequerimentoModel.objects.get(pk=id_requerimento)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
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
                       'id_beneficio': beneficio_id, 'id_agendamento': id_agendamento, 'id_usuario': id_usuario})

    def post(self, request, id_beneficio=None):
        beneficio = BeneficioModel.objects.get(pk=id_beneficio)
        usuario_logado = User.objects.get(pk=request.user.id)
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
            id_requerimento = ""

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
            tipo_msg = 'green'
            return render(request, self.template,
                          {'msg': msg, 'tipo_msg': tipo_msg, 'beneficio_descricao': beneficio.descricao, 'id_usuario': usuario_logado.id,
                           'id_beneficio': id_beneficio})
        else:
            print(form_requerimento.errors)
            beneficio = BeneficioModel.objects.get(pk=id_beneficio)
            beneficio_descricao = beneficio.descricao

        return render(request, self.template,
                      {'form_requerimento': form_requerimento, 'form_agendamento': form_agendamento,
                       'beneficio_descricao': beneficio_descricao,
                       'method': 'post', 'id_beneficio': id_beneficio, 'id_usuario': usuario_logado.id})


def RequerimentoDelete(request, id):
    requerimento = RequerimentoModel.objects.get(pk=id)
    requerimento.delete()
    return HttpResponseRedirect('/')


def ApresentaAgendamentos(request):
    agendamentos = AgendamentoModel.objects.all().order_by('data_pericia')
    dados, page_range, ultima = pagination(agendamentos, request.GET.get('page'))
    return render(request, 'listas/tabela_agendamentos.html', {'dados': dados, 'page_range': page_range, 'ultima': ultima})


def ApresentaAgendamentosMedico(request):
    if request.GET or 'page' in request.GET:
        if request.GET.get('data_inicio'):
            print(str(request.GET.get('data_inicio')))
            data_inicio = str(request.GET.get('data_inicio')).split('/')
            inicio_ano, inicio_mes, inicio_dia = data_inicio[2], data_inicio[1], data_inicio[0]
            data_inicio_formatada = str(inicio_ano + "-" + inicio_mes + "-" + inicio_dia)
            data_fim = str(request.GET.get('data_fim')).split('/')
            fim_ano, fim_mes, fim_dia = data_fim[2], data_fim[1], data_fim[0]
            data_fim_formatada = str(fim_ano + "-" + fim_mes + "-" + fim_dia)
            agendamentos = AgendamentoModel.objects.filter(data_pericia__range=(data_inicio_formatada, data_fim_formatada)).order_by('data_pericia')
        else:
            agendamentos = AgendamentoModel.objects.filter(data_pericia=date.today()).order_by('data_pericia')
    else:
        agendamentos = AgendamentoModel.objects.filter(data_pericia=date.today()).order_by('data_pericia')

    dados, page_range, ultima = pagination(agendamentos, request.GET.get('page'))
    return render(request, 'listas/tabela_agendamentos.html',
                  {'dados': dados, 'page_range': page_range, 'ultima': ultima,
                   'data_inicio': request.GET.get('data_inicio'),
                   'data_fim': request.GET.get('data_fim')})
