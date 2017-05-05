# coding:utf-8
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from issem.models import RequerimentoModel, AgendamentoModel, BeneficioModel, SeguradoModel, ParametrosConfiguracaoModel
from issem.forms import RequerimentoForm
from django.views.generic.base import View
from datetime import date, timedelta, datetime
from django.contrib.auth.models import User
from issem.views.pagination import pagination
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from issem_project.settings import STATIC_URL


#TODO: REFATORAR CÓDIGO


class RequerimentoView(View):
    template = 'cruds/requerimento.html'
    template_lista = 'lista/requerimentos.html'

    def get(self, request, id=None, id_beneficio=None, msg=None, tipo_msg=None):
        context_dict = {}
        try:
            usuario_logado = User.objects.get(pk=request.user.id)
        except:
            raise Http404("Usuário não encontrado.")
        id_usuario = usuario_logado.id
        if id_beneficio:
            try:
                beneficio = BeneficioModel.objects.get(pk=id_beneficio)
            except:
                raise Http404("Benefício não encontrado.")
            beneficio_descricao = beneficio.descricao
            beneficio_id = beneficio.id
        else:
            beneficio_descricao = None
            beneficio_id = None
        if id:
            try:
                requerimento = RequerimentoModel.objects.get(pk=id)
                # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            except:
                raise Http404("Requerimento não encontrado.")
            beneficio_id = requerimento.beneficio.id
            beneficio_descricao = requerimento.beneficio.descricao
            form = RequerimentoForm(instance=requerimento)
        else:
            form = RequerimentoForm()  # MODO CADASTRO: recebe o formulário vazio]

        context_dict['form'] = form
        context_dict['id'] = id
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        context_dict['beneficio_descricao'] = beneficio_descricao
        context_dict['id_beneficio'] = beneficio_id
        context_dict['id_usuario'] = id_usuario
        return render(request, self.template, context_dict)

    def post(self, request, id_beneficio=None, msg=None, tipo_msg=None):
        context_dict = {}
        try:
            beneficio = BeneficioModel.objects.get(pk=id_beneficio)
        except:
            raise Http404("Benefício não encontrado.")
        try:
            usuario_logado = User.objects.get(pk=request.user.id)
        except:
            raise Http404("Usuário não encontrado.")
        id_usuario = usuario_logado.id
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            try:
                requerimento = RequerimentoModel.objects.get(pk=id)
            except:
                raise Http404("Requerimento não encontrado.")
            form = RequerimentoForm(instance=requerimento, data=request.POST)
        else:  # CADASTRO NOVO
            id = None
            form = RequerimentoForm(data=request.POST)

        #TODO: esse 'form.save()' não deveria estar ao final do código, pois existem invalidades no meio do código
        if form.is_valid():
            form.save()
            requerimento = RequerimentoModel.objects.latest('id')
            id = requerimento.id
            agendamento = AgendamentoModel()
            consulta_parametros = ParametrosConfiguracaoModel.objects.get(id=1)

            dias_gap_agendamento = int(consulta_parametros.gap_agendamento)
            prazo_pericia_final = requerimento.data_final_afastamento + timedelta(days=dias_gap_agendamento)

            tempo_dias_afastamento = requerimento.data_final_afastamento - requerimento.data_inicio_afastamento
            data_admissao = SeguradoModel.objects.get(pk=id_usuario).data_admissao
            data_admissao_mais_um_ano = data_admissao + timedelta(days=consulta_parametros.tempo_minimo_exercicio)

            if date.today() > data_admissao_mais_um_ano:
                if date.today() > prazo_pericia_final:
                    msg = define_mensagem_prazo_expirado(prazo_pericia_final)
                    # DELETAR O REQUERIMENTO SEM AGENDAMENTO GERADO #
                    query = RequerimentoModel.objects.get(pk=id)
                    query.delete()
                    return render(request, self.template, {'msg': msg, 'beneficio_descricao': beneficio.descricao,
                                                           'id_usuario': id_usuario})
                else:
                    for dia in range(1, dias_gap_agendamento + 2):
                        if dia <= dias_gap_agendamento:
                            possivel_data_pericia = requerimento.data_final_afastamento + timedelta(days=dia)
                            data_pericia, hora_pericia = verifica_data_hora_pericia(possivel_data_pericia,
                                                                                    consulta_parametros)
                            if (data_pericia != "") and (hora_pericia != "") and (data_pericia != date.today()):
                                agendamento.data_agendamento = date.today()
                                agendamento.data_pericia = data_pericia
                                agendamento.hora_pericia = str(hora_pericia)
                                agendamento.requerimento_id = id
                                agendamento.save()
                                # O ÚLTIMO REQUERIMENTO CADASTRADO CONTÉM UM AGENDAMENTO #
                                obj_requerimento = form.save(commit=False)
                                obj_requerimento.possui_agendamento = True
                                obj_requerimento.save()
                                hora_pericia_msg = str(hora_pericia)
                                msg_valida = define_mensagem_consulta(data_pericia, hora_pericia_msg[:len(
                                    hora_pericia_msg) - 3] + "h", beneficio)

                                return render(request, self.template,
                                              {'msg_valida': msg_valida, 'beneficio_descricao': beneficio.descricao,
                                               'id_usuario': id_usuario, 'id_agendamento': agendamento.id,
                                               'id_beneficio': beneficio.id})
                        else:
                            msg = ("Não há datas disponíveis para consulta. Entre em contato com o ISSEM")
                            tipo_msg = "yellow"
                            return render(request, self.template,
                                          {'msg': msg, 'tipo_msg': tipo_msg,
                                           'beneficio_descricao': beneficio.descricao,
                                           'id_usuario': id_usuario, 'obj_agendamento': agendamento.id})

            else:
                msg = ("Servidor deve ter mais de 1(UM) ano de exercício para realizar agendamentos automáticos."
                       " Entre em contato com o ISSEM")
                tipo_msg = "red"
                # DELETAR O REQUERIMENTO SEM AGENDAMENTO GERADO #
                query = RequerimentoModel.objects.get(pk=id)
                query.delete()

                return render(request, self.template,
                              {'msg': msg, 'tipo_msg': tipo_msg, 'beneficio_descricao': beneficio.descricao,
                               'id_usuario': id_usuario})

            # DELETAR O REQUERIMENTO SEM AGENDAMENTO GERADO #
            query = RequerimentoModel.objects.get(pk=id)
            query.delete()

            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id, 'id_beneficio': beneficio.id,
                                               'beneficio_descricao': beneficio.descricao, 'id_usuario': id_usuario,
                                               'msg': msg})


def GeraComprovanteAgendamento(request, msg=None, id_usuario=None, id_agendamento=None):
    seguado = SeguradoModel.objects.get(pk=id_usuario)
    agendamento = AgendamentoModel.objects.get(pk=id_agendamento)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="comprovante_agendamento.pdf"'
    p = canvas.Canvas(response)
    p.setLineWidth(.1)
    msg1 = msg[:msg.find('.') + 1]
    msg2 = msg[msg.find('.') + 2:]
    prefix = 'https://' if request.is_secure() else 'http://'
    image_url = prefix + request.get_host() + STATIC_URL + "/images/issem_comprovante.jpg"
    p.drawImage(image_url, 250, 750, mask=[0, 255, 0, 255, 0, 255], width=60, height=60)

    p.drawString(50, 730, msg1)
    qtdLinhas = len(msg2) / 70
    linhaInicial = 728
    psInicial = 0
    psFinal = 80
    i = 0
    p.setFont("Helvetica", 11)
    print(qtdLinhas)
    if qtdLinhas == 0:
        linhaInicial -= 12
        p.drawString(50, linhaInicial, msg2)
    while i < qtdLinhas:
        linhaInicial -=12
        p.drawString(50, linhaInicial, msg2[psInicial:psFinal])
        psInicial += 80
        psFinal += 80
        i +=1
    linhaInicial -=10
    p.drawString(50, linhaInicial, "_______________________________________")
    p.setFont("Helvetica", 10)
    p.drawString(50, linhaInicial-10, "Agendado para: " + seguado.nome + (" (CPF: " + seguado.cpf + ")"))
    p.drawString(50, linhaInicial-20,
                 "Data atendimento: " + str(agendamento.data_pericia)[8:] + "/" + str(agendamento.data_pericia)[
                                                                                  5:7] + "/" +
                 str(agendamento.data_pericia)[0:4])
    p.drawString(50, linhaInicial-30, "Horário da consulta: " + str(agendamento.hora_pericia)[:5] + "h")
    p.setFont("Helvetica", 8)
    p.drawString(50, linhaInicial-40, "_______________________________________")
    p.drawString(50, linhaInicial-50, "Documento gerado em: " + str(datetime.now().strftime("%d/%m/%Y às %H:%M:%S")))
    p.setFont("Helvetica", 6)
    p.drawString(50, linhaInicial-60, "*NÃO É NECESSÁRIO IMPRIMIR ESTE DOCUMENTO")
    p.showPage()
    p.save()
    return response


def RequerimentoAgendamentoDelete(request, id_requerimento, id_agendamento):
    requerimento = RequerimentoModel.objects.get(pk=id_requerimento)
    requerimento.delete()
    return HttpResponseRedirect('/')


def RequerimentoSemAgendamentoDelete(request, id):
    requerimento = RequerimentoModel.objects.get(pk=id)
    requerimento.delete()
    msg = "Solicitação de agendamento excluída com sucesso."
    tipo_msg = "green"
    return ApresentaRequerimentosSemAgendamento(request, msg, tipo_msg)


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
    obs_beneficio = beneficio.observacao.encode('utf-8').strip()
    return ("Sua consulta ficou agendada para %s/%s/%s às %s. %s") % (
        dia, mes, ano, str(hora_pericia), str(obs_beneficio))


def define_mensagem_prazo_expirado(prazo_pericia_final):
    texto_msg = str(prazo_pericia_final)
    texto_msg = texto_msg.split("-")
    dia = texto_msg[2]
    mes = texto_msg[1]
    ano = texto_msg[0]
    return ("O prazo para requerimento venceu dia %s/%s/%s. Consulte o ISSEM para mais informações.") % (dia, mes, ano)


def ApresentaAgendamentos(request, msg=None, tipo_msg=None):
    var_controle = 0
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
            var_controle = 1

        else:
            agendamentos = AgendamentoModel.objects.all().order_by('data_pericia')

    else:
        agendamentos = AgendamentoModel.objects.all().order_by('data_pericia')

    dados, page_range, ultima = pagination(agendamentos, request.GET.get('page'))
    return render(request, 'listas/tabela_agendamentos.html',
                  {'dados': dados, 'page_range': page_range, 'ultima': ultima, 'var_controle' : var_controle, 'data_inicio': request.GET.get('data_inicio'),
                   'data_fim': request.GET.get('data_fim')})


def ApresentaRequerimentosSemAgendamento(request):
    var_controle = 0
    if request.GET or 'page' in request.GET:
        if request.GET.get('data_inicio'):
            print(str(request.GET.get('data_inicio')))
            data_inicio = str(request.GET.get('data_inicio')).split('/')
            inicio_ano, inicio_mes, inicio_dia = data_inicio[2], data_inicio[1], data_inicio[0]
            data_inicio_formatada = str(inicio_ano + "-" + inicio_mes + "-" + inicio_dia)
            data_fim = str(request.GET.get('data_fim')).split('/')
            fim_ano, fim_mes, fim_dia = data_fim[2], data_fim[1], data_fim[0]
            data_fim_formatada = str(fim_ano + "-" + fim_mes + "-" + fim_dia)
            agendamentos = RequerimentoModel.objects.filter(
                data_requerimento__range=(data_inicio_formatada, data_fim_formatada), possui_agendamento=False).order_by('data_requerimento')
            var_controle = 1

        else:
            agendamentos = RequerimentoModel.objects.filter(possui_agendamento=False).order_by('data_requerimento')

    else:
        agendamentos = RequerimentoModel.objects.filter(possui_agendamento=False).order_by('data_requerimento')

    dados, page_range, ultima = pagination(agendamentos, request.GET.get('page'))
    return render(request, 'listas/tabela_requerimentos_sem_agendamento.html',
                  {'dados': dados, 'page_range': page_range, 'ultima': ultima, 'var_controle' : var_controle,
                   'data_inicio': request.GET.get('data_inicio'),
                   'data_fim': request.GET.get('data_fim')})
