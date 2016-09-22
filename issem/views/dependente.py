# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import DependenteModel
from issem.forms import DependenteForm
from django.views.generic.base import View
from issem.models import EstadoModel


class DependenteView(View):
    template = 'dependente.html'

    def get(self, request, id=None):
        if id:
            dependente = DependenteModel.objects.get(
                pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = DependenteForm(instance=dependente)
        else:
            form = DependenteForm()  # MODO CADASTRO: recebe o formulário vazio
        estados = EstadoModel.objects.all()
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id, 'estados': estados})

    def post(self, request):
        if not request.POST['id']:  # CADASTRO NOVO
            id = None
            form = DependenteForm(data=request.POST)
        else:  # EDIÇÃO
            id = request.POST['id']
            dependente = DependenteModel.objects.get(pk=id)
            form = DependenteForm(instance=dependente, data=request.POST)

        if form.is_valid():
            dependente = form.save(commit=False)
            dependente.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post'})


def DependenteDelete(request, id):
    dependente = DependenteModel.objects.get(pk=id)
    dependente.delete()
    return HttpResponseRedirect('/')
