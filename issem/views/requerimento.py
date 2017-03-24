# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import RequerimentoModel, AgendamentoModel, ConsultaParametrosModel, BeneficioModel
from issem.forms import RequerimentoForm
from django.views.generic.base import View
from datetime import date, timedelta
from django.contrib.auth.models import User
from issem.views.pagination import pagination


class RequerimentoView(View):
    template = 'requerimento.html'

    def get(self, request, id=None, id_beneficio=None):
        usuario_logado = User.objects.get(pk=request.user.id)
        id_usuario = usuario_logado.id
        if id_beneficio:
            beneficio = BeneficioModel.objects.get(pk=id_beneficio)
            beneficio_descricao = beneficio.descricao
            beneficio_id = beneficio.id
        else:
            beneficio_descricao = ""
            beneficio_id = ""
        if id:
            requerimento = RequerimentoModel.objects.get(
                pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            beneficio_id = requerimento.beneficio.id
            beneficio_descricao = requerimento.beneficio.descricao
            form = RequerimentoForm(instance=requerimento)

        else:
            form = RequerimentoForm()  # MODO CADASTRO: recebe o formulário vazio]
        print(form)
        return render(request, self.template,
                      {'form': form, 'method': 'get', 'id': id, 'beneficio_descricao': beneficio_descricao,
                       'id_beneficio': beneficio_id, 'id_usuario': id_usuario})

    def post(self, request, id_beneficio=None):
        beneficio = BeneficioModel.objects.get(pk=id_beneficio)
        usuario_logado = User.objects.get(pk=request.user.id)
        id_usuario = usuario_logado.id
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            requerimento = RequerimentoModel.objects.get(pk=id)
            form = RequerimentoForm(instance=requerimento, data=request.POST)
        else:  # CADASTRO NOVO
            id = None
            form = RequerimentoForm(data=request.POST)
        if form.is_valid():
            form.save()
            requerimento = RequerimentoModel.objects.latest('id')
            id = requerimento.id
            agendamento_form = AgendamentoModel()
            consulta_parametros = ConsultaParametrosModel.objects.get(id=1)

            dias_gap_agendamento = int(consulta_parametros.gap_agendamento)
            prazo_pericia_final = requerimento.data_final_afastamento + timedelta(days=dias_gap_agendamento)

            tempo_dias_afastamento = requerimento.data_final_afastamento - requerimento.data_inicio_afastamento
            if tempo_dias_afastamento < timedelta(days=15):
                msg = "O prazo para agendamento automatico via sistema ISSEM é de no mínimo 15(quinze) dias de afastamento."
                return render(request, self.template, {'msg': msg, 'beneficio_descricao': beneficio.descricao
                    , 'id_usuario': id_usuario})
            else:
                if date.today() > prazo_pericia_final:
                    msg = define_mensagem_prazo_expirado(prazo_pericia_final)
                    return render(request, self.template, {'msg': msg, 'beneficio_descricao': beneficio.descricao, 'id_usuario': id_usuario})
                else:
                    for dia in range(1, dias_gap_agendamento + 2):
                        if dia <= dias_gap_agendamento:
                            possivel_data_pericia = requerimento.data_final_afastamento + timedelta(days=dia)
                            data_pericia, hora_pericia = verifica_data_hora_pericia(possivel_data_pericia,consulta_parametros)
                            if (data_pericia != "") and (hora_pericia != "") and (data_pericia != date.today()):
                                agendamento_form.data_agendamento = date.today()
                                agendamento_form.data_pericia = data_pericia
                                agendamento_form.hora_pericia = str(hora_pericia)
                                agendamento_form.requerimento_id = id
                                agendamento_form.save()
                                # O ÚLTIMO REQUERIMENTO CADASTRADO CONTÉM UM AGENDAMENTO #
                                obj_requerimento = form.save(commit=False)
                                obj_requerimento.possui_agendamento = True
                                obj_requerimento.save()
                                msg = define_mensagem_consulta(data_pericia, hora_pericia, beneficio)
                                return render(request, self.template,
                                              {'msg': msg, 'beneficio_descricao': beneficio.descricao, 'id_usuario' : id_usuario})
                                break
                        else:
                            msg = ("Não há datas disponíveis para consulta. Entre em contato com o ISSEM")
                            return render(request, self.template, {'msg': msg, 'beneficio_descricao': beneficio.descricao, 'id_usuario': id_usuario})
                            break
                return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id, 'id_beneficio': beneficio.id,
                                               'beneficio_descricao': beneficio.descricao, 'id_usuario' : id_usuario})


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
        inicio_atendimento_hora = consulta_parametros.inicio_atendimento.strftime("%H")
        inicio_atendimento_minuto = consulta_parametros.inicio_atendimento.strftime("%M")
        inicio_atendimento_hora = timedelta(hours=int(inicio_atendimento_hora), minutes=int(inicio_atendimento_minuto))
        hora_pericia = inicio_atendimento_hora + tempo_somar_hora_de_abertura
    return (data_pericia, hora_pericia)


def define_mensagem_consulta(data_pericia, hora_pericia, beneficio):
    texto_msg = str(data_pericia)
    texto_msg = texto_msg.split("-")
    dia = texto_msg[2]
    mes = texto_msg[1]
    ano = texto_msg[0]
    obs_beneficio = beneficio.observacao
    return ("Sua consulta ficou agendada para %s/%s/%s às %s. %s") % (dia, mes, ano, str(hora_pericia), str(obs_beneficio))


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


def ApresentaRequerimentosSemAgendamento(request):

    requerimentos = RequerimentoModel.objects.filter(possui_agendamento = False)
    dados, page_range, ultima = pagination(requerimentos, request.GET.get('page'))
    return render(request, 'tabela_requerimentos_sem_agendamento.html', {'dados': dados, 'page_range' : page_range, 'ultima' : ultima})