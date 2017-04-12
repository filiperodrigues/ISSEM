# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import TipoDependenteModel
from issem.forms import TipoDependenteForm
from django.views.generic.base import View


class TipoDependenteView(View):
    template = 'cruds/tipo_dependente.html'

    def get(self, request, id=None):
        if id:
            tipo_dependente = TipoDependenteModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = TipoDependenteForm(instance=tipo_dependente)
        else:
            form = TipoDependenteForm()  # MODO CADASTRO: recebe o formulário vazio
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id})

    def post(self, request):
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            tipo_dependente = TipoDependenteModel.objects.get(pk=id)
            form = TipoDependenteForm(instance=tipo_dependente, data=request.POST)
        else:  # CADASTRO NOVO
            id = None
            form = TipoDependenteForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id})


def TipoDependenteDelete(request, id):
    tipo_dependente = TipoDependenteModel.objects.get(pk=id)
    tipo_dependente.delete()
    return HttpResponseRedirect('/')
