# coding:utf-8
from django.http import Http404
from django.shortcuts import render
from issem.models import ProcedimentoMedicoModel
from issem.forms import ProcedimentoMedicoForm
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from issem.views.pagination import pagination


class ProcedimentoMedicoView(View):
    template = 'cruds/procedimento_medico.html'
    template_lista = 'lista/procedimentos_medicos.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}
        if id:
            try:
                procedimento_medico = ProcedimentoMedicoModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            except:
                raise Http404("Procedimento Médico não encontrado.")
            form = ProcedimentoMedicoForm(instance=procedimento_medico)
        else:
            form = ProcedimentoMedicoForm()  # MODO CADASTRO: recebe o formulário vazio

        context_dict['form'] = form
        context_dict['id'] = id
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template, context_dict)

    @method_decorator(user_passes_test(group_test))
    def post(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        valido = False
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            try:
                procedimento_medico = ProcedimentoMedicoModel.objects.get(pk=id)
            except:
                raise Http404("Procedimento Médico não encontrado.")
            form = ProcedimentoMedicoForm(instance=procedimento_medico, data=request.POST)
            if form.is_valid():
                form.save()
                msg = 'Alterações realizadas com sucesso!'
                tipo_msg = 'green'
                valido = True
        else:  # CADASTRO NOVO
            id = None
            form = ProcedimentoMedicoForm(data=request.POST)
            if form.is_valid():
                form.save()
                msg = 'Procedimento Médico cadastrado com sucesso!'
                tipo_msg = 'green'
                form = ProcedimentoMedicoForm()
                valido = True

        if not valido:
            print(form.errors)
            msg = 'Erros encontrados!'
            tipo_msg = 'red'

        context_dict['form'] = form
        context_dict['id'] = id
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template, context_dict)


    @classmethod
    @method_decorator(user_passes_test(group_test))
    def ProcedimentoMedicoDelete(self, request, id=None):
        try:
            procedimento_medico = ProcedimentoMedicoModel.objects.get(pk=id)
        except:
            raise Http404("Procedimento Médico CID não encontrado.")
        procedimento_medico.excluido = True
        procedimento_medico.save()
        msg = 'Exclusão efetuada com sucesso!'
        tipo_msg = 'green'
        return self.ListaProcedimentosMedicos(request, msg, tipo_msg)

    @classmethod
    @method_decorator(user_passes_test(group_test))
    def ListaProcedimentosMedicos(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        var_controle = 0
        if request.GET or 'page' in request.GET:
            if request.GET.get('filtro'):
                cid1 = ProcedimentoMedicoModel.objects.filter(descricao__contains=request.GET.get('filtro'), excluido=0)
                cid2 = ProcedimentoMedicoModel.objects.filter(codigo__contains=request.GET.get('filtro'), excluido=0)
                cid3 = ProcedimentoMedicoModel.objects.filter(valor__contains=request.GET.get('filtro'), excluido=0)
                procedimentos_medicos = list(cid1) + list(cid2) + list(cid3)
                procedimentos_medicos = list(set(procedimentos_medicos))
                var_controle = 1

            else:
                procedimentos_medicos = ProcedimentoMedicoModel.objects.filter(excluido=False)
        else:
            procedimentos_medicos = ProcedimentoMedicoModel.objects.filter(excluido=False)

        dados, page_range, ultima = pagination(procedimentos_medicos, request.GET.get('page'))
        context_dict['dados'] = dados
        context_dict['page_range'] = page_range
        context_dict['ultima'] = ultima
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        context_dict['var_controle'] = var_controle
        context_dict['filtro'] = request.GET.get('filtro')
        return render(request, self.template_lista, context_dict)
