# coding:utf-8
from django.http import Http404
from django.shortcuts import render
from issem.models import RequerimentoModel, AgendamentoModel, BeneficioModel
from issem.forms import RequerimentoForm, AgendamentoForm
from django.views.generic.base import View
from datetime import date, datetime


class GeraAgendamentoServidorView(View):
    template = 'cruds/requerimento_servidor.html'
    template_lista = "listas/tabela_agendamentos.html"
    template_painel = 'paineis/funcionario_pagina.html'

    def get(self, request, id_requerimento=None, id_beneficio=None, id_agendamento=None, msg=None, tipo_msg=None):
        context_dict = {}
        var_controle = "Edicão ou definição de agendamento para um requerimento"
        if id_beneficio:
            try:
                beneficio = BeneficioModel.objects.get(pk=id_beneficio)
            except:
                raise Http404("Benefício não encontrado.")
            beneficio_descricao = beneficio.descricao
            beneficio_id = beneficio.id
        else:
            beneficio_descricao = ""
            beneficio_id = ""
        if id_requerimento:
            try:
                # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
                requerimento = RequerimentoModel.objects.get(pk=id_requerimento)
            except:
                raise Http404("Requerimento não encontrado.")
            agendamento = AgendamentoModel()
            beneficio_id = requerimento.beneficio.id
            beneficio_descricao = requerimento.beneficio.descricao
            form_requerimento = RequerimentoForm(instance=requerimento)
            form_agendamento = AgendamentoForm(instance=agendamento)
        else:
            form_requerimento = RequerimentoForm()  # MODO CADASTRO: recebe o formulário vazio]
            form_agendamento = AgendamentoForm()

        context_dict['form_requerimento'] = form_requerimento
        context_dict['form_agendamento'] = form_agendamento
        context_dict['id_requerimento'] = id_requerimento
        context_dict['beneficio_descricao'] = beneficio_descricao
        context_dict['id_beneficio'] = beneficio_id
        context_dict['id_agendamento'] = id_agendamento
        context_dict['var_controle'] = var_controle
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template, context_dict)

    def post(self, request, id_requerimento=None, msg=None, tipo_msg=None):
        context_dict = {}
        if request.POST['id']:  # EDIÇÃO
            try:
                requerimento = RequerimentoModel.objects.get(pk=id_requerimento)
            except:
                raise Http404("Requerimento não encontrado.")
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

            try:
                requerimento = RequerimentoModel.objects.get(pk=id_requerimento)
            except:
                raise Http404("Requerimento não encontrado")

            form_agendamento_model = AgendamentoModel()
            form_agendamento_model.requerimento_id = id_requerimento
            form_agendamento_model.data_agendamento = date.today()
            data_pericia_form = form_agendamento._raw_value('data_pericia')
            data_pericia_split = data_pericia_form.split('/')
            data_pericia = datetime(int(data_pericia_split[2]), int(data_pericia_split[1]), int(data_pericia_split[0]))
            form_agendamento_model.data_pericia = data_pericia
            hora_pericia = form_agendamento._raw_value('hora_pericia')
            form_agendamento_model.hora_pericia = hora_pericia
            # TODO: Verificar se não precisa de "if form.is_valid()"
            form_agendamento_model.save()
            # TODO: Verificar se a linha abaixo é necessária
            # obj = requerimento.save(commit=False)

            requerimento.possui_agendamento = True
            # TODO: Verificar se não precisa de "if form.is_valid()"
            requerimento.save()

            msg_cadastro_concluido = self.DefineMensagemAgendamento(data_pericia, hora_pericia)

            msg = msg_cadastro_concluido
            tipo_msg = 'green'
            context_dict['beneficio_descricao'] = requerimento.beneficio.descricao
        else:
            print(form_requerimento.errors)
            msg = 'Erros encontrados!'
            tipo_msg = 'red'
            try:
                requerimento = RequerimentoModel.objects.get(pk=id_requerimento)
            except:
                raise Http404("Requerimento não encontrado.")

        context_dict['form_requerimento'] = form_requerimento
        context_dict['form_agendamento'] = form_agendamento
        context_dict['id_beneficio'] = requerimento.beneficio_id
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template, context_dict)

    @classmethod
    def DefineMensagemAgendamento(self, data_agendamento, hora_pericia):
        texto_msg = str(data_agendamento)
        texto_msg = texto_msg.split("-")
        dia = texto_msg[2][:2]
        mes = texto_msg[1]
        ano = texto_msg[0]
        return "Consulta agendada para %s/%s/%s às %s" % (dia, mes, ano, str(hora_pericia))

    @classmethod
    def RequerimentoDelete(self, request, id=None):
        context_dict = {}
        try:
            requerimento = RequerimentoModel.objects.get(pk=id)
        except:
            raise Http404("Requerimento não encontrado.")
        requerimento.delete()
        msg = 'Exclusão efetuada com sucesso!'
        tipo_msg = 'green'
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template_painel, context_dict)

    @classmethod
    def ApresentaAgendamentos(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        context_dict['agendamentos'] = AgendamentoModel.objects.all().order_by('data_pericia')
        return render(request, self.template_lista, context_dict)
