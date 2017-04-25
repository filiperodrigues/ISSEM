# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import ProcedimentoMedicoModel
from issem.forms import ProcedimentoMedicoForm
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from issem.views.pagination import pagination


class ProcedimentoMedicoView(View):
    template = 'cruds/procedimento_medico.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    @method_decorator(user_passes_test(group_test))

    def get(self, request, id=None):
        if id:
            procedimento_medico = ProcedimentoMedicoModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = ProcedimentoMedicoForm(instance=procedimento_medico)
        else:
            form = ProcedimentoMedicoForm()  # MODO CADASTRO: recebe o formulário vazio
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id})

    def post(self, request):
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            procedimento_medico = ProcedimentoMedicoModel.objects.get(pk=id)
            form = ProcedimentoMedicoForm(instance=procedimento_medico, data=request.POST)
        else:  # CADASTRO NOVO
            id = None
            form = ProcedimentoMedicoForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id})


def ProcedimentoMedicoDelete(request, id):
    procedimento_medico = ProcedimentoMedicoModel.objects.get(pk=id)
    procedimento_medico.excluido = True
    procedimento_medico.save()
    return ListaProcedimentosMedicos(request, msg="Procedimento Médico excluído com sucesso!", tipo_msg="green")


def ListaProcedimentosMedicos(request, msg=None, tipo_msg=None):
    if request.GET:
        pm1 = ProcedimentoMedicoModel.objects.filter(descricao__icontains=request.GET.get('campo'), excluido=0)
        pm2 = ProcedimentoMedicoModel.objects.filter(valor__icontains=request.GET.get('campo'), excluido=0)
        pm3 = ProcedimentoMedicoModel.objects.filter(codigo__contains=request.GET.get('campo'), excluido=0)
        procedimentos_medico = list(pm1) + list(pm2) + list(pm3)
        procedimentos_medico = list(set(procedimentos_medico))
    else:
        procedimentos_medico = ProcedimentoMedicoModel.objects.filter(excluido=False)

    dados, page_range, ultima = pagination(procedimentos_medico, request.GET.get('page'))
    return render(request, 'listas/procedimentos_medicos.html', {'dados': dados, 'page_range':page_range, 'ultima': ultima, 'msg': msg, 'tipo_msg': tipo_msg})