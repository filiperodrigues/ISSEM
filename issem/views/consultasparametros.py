# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import ConsultasParametrosModel
from issem.forms import ConsultasParametrosForm
from django.views.generic.base import View


class ConstultasParametrosView(View):
    template = 'consultas_parametros.html'

    def get(self, request, id=None):
        if id:
            consultas_parametros = ConsultasParametrosModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = ConsultasParametrosForm(instance=consultas_parametros)
        else:
            form = ConsultasParametrosForm()  # MODO CADASTRO: recebe o formulário vazio
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id})

    def post(self, request):
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            consultas_parametros = ConsultasParametrosModel.objects.get(pk=id)
            form = ConsultasParametrosForm(instance=consultas_parametros, data=request.POST)
        else:  # CADASTRO NOVO
            id = None
            form = ConsultasParametrosForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post'})


def ConsultasParametrosDelete(request, id):
    consultas_parametros = ConsultasParametrosModel.objects.get(pk=id)
    consultas_parametros.delete()
    return HttpResponseRedirect('/')
