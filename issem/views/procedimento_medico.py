# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import ProcedimentoMedicoModel
from issem.forms import ProcedimentoMedicoForm
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


class ProcedimentoMedicoView(View):
    template = 'procedimento_medico.html'

    def group_test(user):
        return user.groups.filter(name='Servidor')

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
    procedimento_medico.delete()
    return HttpResponseRedirect('/')


def ListaProcedimentosMedicos(request):
    context_dict = {}
    context_dict['procedimentos_medicos'] = ProcedimentoMedicoModel.objects.all()
    return render(request, 'procedimentos_medicos.html', context_dict)