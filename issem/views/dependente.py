# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import DependenteModel
from issem.forms import DependenteForm
from django.views.generic.base import View
from issem.models import EstadoModel, CidadeModel


class DependenteView(View):
    template = 'dependente.html'

    def get(self, request, id=None):
        if id:
            dependente = DependenteModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            # estado = EstadoModel.objects.get(id=CidadeModel.objects.get(id=dependente.cidade_atual))
            form = DependenteForm(instance=dependente)
        else:
            form = DependenteForm()  # MODO CADASTRO: recebe o formulário vazio
        # return render(request, self.template, {'form': form, 'method': 'get', 'id': id, 'estado': estado})
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id})

    def post(self, request):
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            dependente = DependenteModel.objects.get(pk=id)
            form = DependenteForm(instance=dependente, data=request.POST)
        else:  # CADASTRO NOVO
            id = None
            form = DependenteForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id})


def DependenteDelete(request, id):
    dependente = DependenteModel.objects.get(pk=id)
    dependente.delete()
    return HttpResponseRedirect('/')
