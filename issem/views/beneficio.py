# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import BeneficioModel
from issem.forms import BeneficioForm
from django.views.generic.base import View


class BeneficioView(View):
    template = 'beneficio.html'

    def get(self, request, id=None):
        if id:
            beneficio = BeneficioModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = BeneficioForm(instance=beneficio)
        else:
            form = BeneficioForm()  # MODO CADASTRO: recebe o formulário vazio
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id})

    def post(self, request):
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            beneficio = BeneficioModel.objects.get(pk=id)
            form = BeneficioForm(instance=beneficio, data=request.POST)
        else:  # CADASTRO NOVO
            id = None
            form = BeneficioForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id})


def BeneficioDelete(request, id):
    beneficio = BeneficioModel.objects.get(pk=id)
    beneficio.delete()
    return HttpResponseRedirect('/')
