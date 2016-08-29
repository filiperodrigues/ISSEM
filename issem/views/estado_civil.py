# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import EstadoCivilModel
from issem.forms import EstadoCivilForm
from django.views.generic.base import View


class EstadoCivilView(View):
    template = 'estado_civil.html'

    def get(self, request, id=None):
        if id:
            estado_civil = EstadoCivilModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = EstadoCivilForm(instance=estado_civil)
        else:
            form = EstadoCivilForm()  # MODO CADASTRO: recebe o formulário vazio
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id})

    def post(self, request):
        if not request.POST['id']:  # CADASTRO NOVO
            id = None
            form = EstadoCivilForm(data=request.POST)
        else:  # EDIÇÃO
            id = request.POST['id']
            estado_civil = EstadoCivilModel.objects.get(pk=id)
            form = EstadoCivilForm(instance=estado_civil, data=request.POST)

        if form.is_valid():
            estado_civil = form.save(commit=False)
            estado_civil.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id})


def EstadoCivilDelete(request, id):
    estado_civil = EstadoCivilModel.objects.get(pk=id)
    estado_civil.delete()
    return HttpResponseRedirect('/')
