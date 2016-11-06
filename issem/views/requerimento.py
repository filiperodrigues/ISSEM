# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import RequerimentoModel, AgendamentoModel, ConsultaParametrosModel, BeneficioModel
from issem.forms import RequerimentoForm
from django.views.generic.base import View
from datetime import date, timedelta

class RequerimentoView(View):
    template = 'requerimento.html'

    def get(self, request, id=None, id_beneficio=None):
        if id_beneficio:
            beneficio = BeneficioModel.objects.get(pk=id_beneficio)
            beneficio_descricao = beneficio.descricao
            beneficio_id = beneficio.id
        else:
            beneficio_descricao = ""
            beneficio_id = ""
        if id:
            requerimento = RequerimentoModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            beneficio_id = requerimento.beneficio.id
            beneficio_descricao = requerimento.beneficio.descricao
            form = RequerimentoForm(instance=requerimento)

        else:
            form = RequerimentoForm()  # MODO CADASTRO: recebe o formulário vazio]
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id, 'beneficio_descricao' : beneficio_descricao, 'id_beneficio' : beneficio_id})

    def post(self, request, id_beneficio=None):
        beneficio = BeneficioModel.objects.get(pk=id_beneficio)
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            requerimento = RequerimentoModel.objects.get(pk=id)
            form = RequerimentoForm(instance=requerimento, data=request.POST)
        else:  # CADASTRO NOVO
            id = None
            form = RequerimentoForm(data=request.POST)

        if form.is_valid():
            current_user = request.user
            form.segurado = current_user
            form.servidor = current_user
            form.save()
            requerimento = RequerimentoModel.objects.latest('id')
            id = requerimento.id
            agendamento_form = AgendamentoModel()
            consulta_parametros = ConsultaParametrosModel.objects.get(id=1)

            dias_gap_agendamento = int(consulta_parametros.gap_agendamento)
            prazo_pericia_final = requerimento.data_final_afastamento + timedelta(days=dias_gap_agendamento)

            if date.today() > prazo_pericia_final:
                msg = define_mensagem_prazo_expirado(prazo_pericia_final)
                return render(request, self.template, {'msg': msg, 'beneficio_descricao': beneficio.descricao})
            else:
                for dia in range(1, dias_gap_agendamento + 2):
                    if dia <= dias_gap_agendamento:
                        possivel_data_pericia = requerimento.data_final_afastamento + timedelta(days=dia)
                        data_pericia, hora_pericia = verifica_data_hora_pericia(possivel_data_pericia, consulta_parametros)
                        if (data_pericia != "") and (hora_pericia != ""):
                            agendamento_form.data_agendamento = date.today()
                            agendamento_form.data_pericia = data_pericia
                            agendamento_form.hora_pericia = str(hora_pericia)
                            agendamento_form.requerimento_id = id
                            agendamento_form.save()
                            # O ÚLTIMO REQUERIMENTO CADASTRADO CONTÉM UM AGENDAMENTO #
                            obj = form.save(commit=False)
                            obj.possui_agendamento = True
                            obj.save()
                            msg = define_mensagem_consulta(data_pericia, hora_pericia)
                            return render(request, self.template, {'msg': msg, 'beneficio_descricao' : beneficio.descricao})
                            break
                    else:
                        msg = ("Não há datas disponíveis para consulta. Entre em contato com o ISSEM")
                        return render(request, self.template, {'msg': msg, 'beneficio_descricao' : beneficio.descricao})
                        break
            return HttpResponseRedirect('/')

        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id, 'id_beneficio' : beneficio.id, 'beneficio_descricao' : beneficio.descricao})


def RequerimentoAgendamentoDelete(request, id_requerimento, id_agendamento):
    requerimento = RequerimentoModel.objects.get(pk=id_requerimento)
    requerimento.delete()
    return HttpResponseRedirect('/')


def verifica_data_hora_pericia(dia, consulta_parametros):
    data_pericia = ""
    hora_pericia = ""
    qtd_agendamentos_dia = 0
    for data_pericia_dia in AgendamentoModel.objects.filter(data_pericia=dia):
        qtd_agendamentos_dia += 1
    if qtd_agendamentos_dia < consulta_parametros.limite_consultas:
        data_pericia = dia
        tempo_consulta = timedelta(minutes=consulta_parametros.tempo_consulta)
        tempo_espera = timedelta(minutes=consulta_parametros.tempo_espera)
        tempo_somar_hora_de_abertura = (tempo_espera + tempo_consulta) * qtd_agendamentos_dia
        hora_pericia = consulta_parametros.inicio_atendimento + tempo_somar_hora_de_abertura
    return (data_pericia, hora_pericia)


def define_mensagem_consulta(data_pericia, hora_pericia):
    texto_msg = str(data_pericia)
    texto_msg = texto_msg.split("-")
    dia = texto_msg[2]
    mes = texto_msg[1]
    ano = texto_msg[0]
    return ("Sua consulta ficou agendada para %s/%s/%s às %s")%(dia, mes, ano, str(hora_pericia))

def define_mensagem_prazo_expirado(prazo_pericia_final):
    texto_msg = str(prazo_pericia_final)
    texto_msg = texto_msg.split("-")
    dia = texto_msg[2]
    mes = texto_msg[1]
    ano = texto_msg[0]
    return ("O prazo para requerimento venceu dia %s/%s/%s. Consulte o ISSEM para mais informações.") % (dia, mes, ano)

def ApresentaAgendamentos(request):
    context_dict = {}
    context_dict['agendamentos'] = AgendamentoModel.objects.all().order_by('data_pericia')
    return render(request, 'tabela_agendamentos.html', context_dict)
