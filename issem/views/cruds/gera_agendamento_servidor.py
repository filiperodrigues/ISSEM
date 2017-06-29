# coding:utf-8
from django.http import Http404
from django.shortcuts import render
from issem.models import RequerimentoModel, AgendamentoModel, BeneficioModel
from issem.forms import RequerimentoForm, AgendamentoForm
from django.views.generic.base import View
from datetime import date
from issem.views.cruds.requerimento import EnviaEmail


class GeraAgendamentoServidorView(View):
    template = 'cruds/requerimento_servidor.html'
    template_lista = "listas/tabela_agendamentos.html"
    template_painel = 'paineis/funcionario_pagina.html'

    def get(self, request, id_requerimento=None, id_beneficio=None, id_agendamento=None, msg=None, tipo_msg=None):
        print("no get")
        context_dict = {}
        var_controle = True
        if id_beneficio:
            print("1")
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
            context_dict['agendamento_sem_requerimento'] = True
            context_dict['segurado_nome'] = requerimento.segurado.nome
            context_dict['id_usuario'] = request.user.id
            context_dict['segurado_id'] = requerimento.segurado.id
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
        print("no post")
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

            try:
                requerimento = RequerimentoModel.objects.get(pk=id_requerimento)
                form_requerimento = RequerimentoForm(instance=requerimento, data=request.POST)
            except:
                raise Http404("Requerimento não encontrado")

            if form_agendamento.is_valid():
                form_agendamento = form_agendamento.save(commit=False)
                form_agendamento.requerimento_id = requerimento.id
                form_agendamento.data_agendamento = date.today()
                form_agendamento.save()

                # Altera os dados do requerimento é criado #
                form_requerimento.possui_agendamento = True
                form_requerimento.save()

                # form_agendamento = AgendamentoForm()
                # form_requerimento = RequerimentoForm()

                EnviaEmail(requerimento.segurado, form_agendamento.id)

                msg = self.DefineMensagemAgendamento(form_agendamento.data_pericia, form_agendamento.hora_pericia)
                tipo_msg = 'green'

            else:
                msg = "Erros encontrados!"
                tipo_msg = "red"

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
