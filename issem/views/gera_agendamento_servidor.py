# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import RequerimentoModel, AgendamentoModel, ConsultaParametrosModel, BeneficioModel
from issem.forms import RequerimentoForm, AgendamentoForm
from django.views.generic.base import View
from datetime import date, timedelta, datetime


class GeraAgendamentoServidorView(View):
    template = 'requerimento_servidor.html'
    def get(self, request, id_requerimento=None, id_beneficio=None, id_agendamento=None):
        var_controle = "edicão ou definição de agendamento para um requerimento"
        if id_beneficio:
            beneficio = BeneficioModel.objects.get(pk=id_beneficio)
            beneficio_descricao = beneficio.descricao
            beneficio_id = beneficio.id
        else:
            beneficio_descricao = ""
            beneficio_id = ""
        if id_requerimento:
            requerimento = RequerimentoModel.objects.get(pk=id_requerimento)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            agendamento = AgendamentoModel()
            beneficio_id = requerimento.beneficio.id
            beneficio_descricao = requerimento.beneficio.descricao
            form_requerimento = RequerimentoForm(instance=requerimento)
            form_agendamento = AgendamentoForm(instance=agendamento)

        else:
            form_requerimento = RequerimentoForm()  # MODO CADASTRO: recebe o formulário vazio]
            form_agendamento = AgendamentoForm()
        return render(request, self.template, {'form_requerimento': form_requerimento, 'form_agendamento' : form_agendamento,
        'method': 'get', 'id_requerimento': id_requerimento, 'beneficio_descricao' : beneficio_descricao,
        'id_beneficio' : beneficio_id, 'id_agendamento' : id_agendamento, 'var_controle' : var_controle})

    def post(self, request, id_requerimento=None):
        if request.POST['id']:  #
            # id_requerimento = request.POST['id']
            print(id_requerimento)
            requerimento = RequerimentoModel.objects.get(pk=id_requerimento)
            agendamento = AgendamentoModel()
            form_requerimento = RequerimentoForm(instance=requerimento, data=request.POST)
            form_agendamento = AgendamentoForm(instance=agendamento, data=request.POST)
        else:  # CADASTRO NOVO
            form_requerimento = RequerimentoForm(data=request.POST)
            form_agendamento = AgendamentoForm(data=request.POST)

        if form_requerimento.is_valid():
            current_user = request.user
            form_requerimento.segurado = current_user
            form_requerimento.servidor = current_user
            form_requerimento.save()

            requerimento = RequerimentoModel.objects.get(pk = id_requerimento)
            id = requerimento.id

            form_agendamento_model = AgendamentoModel()
            form_agendamento_model.requerimento_id = id
            form_agendamento_model.data_agendamento = date.today()
            data_pericia_form = form_agendamento._raw_value('data_pericia')
            data_pericia_split = data_pericia_form.split('/')
            data_pericia = datetime(int(data_pericia_split[2]), int(data_pericia_split[1]), int(data_pericia_split[0]))
            form_agendamento_model.data_pericia = data_pericia
            hora_pericia = form_agendamento._raw_value('hora_pericia')
            form_agendamento_model.hora_pericia = hora_pericia
            form_agendamento_model.save()
            # obj = requerimento.save(commit=False)

            requerimento.possui_agendamento= True
            requerimento.save()

            msg = define_mensagem_agendamento(data_pericia, hora_pericia)
            return render(request, self.template, {'msg': msg})

        else:
            print(form_requerimento.errors)

        return render(request, self.template, {'form_requerimento' : form_requerimento, 'form_agendamento': form_agendamento,
                                               'method': 'post', 'id_beneficio': requerimento.beneficio_id })

def define_mensagem_agendamento(data_agendamento, hora_pericia):
    texto_msg = str(data_agendamento)
    texto_msg = texto_msg.split("-")
    dia = texto_msg[2][:2]
    mes = texto_msg[1]
    ano = texto_msg[0]
    return ("Consulta agendada para %s/%s/%s às %s") % (dia, mes, ano, str(hora_pericia))

def RequerimentoDelete(request, id):
    requerimento = RequerimentoModel.objects.get(pk=id)
    requerimento.delete()
    return HttpResponseRedirect('/')

def ApresentaAgendamentos(request):
    context_dict = {}
    context_dict['agendamentos'] = AgendamentoModel.objects.all().order_by('data_pericia')
    return render(request, 'tabela_agendamentos.html', context_dict)