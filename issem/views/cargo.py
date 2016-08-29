# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import CargoModel
from issem.forms import CargoForm
from django.views.generic.base import View


class CargoView(View):
    template = 'cargo.html'

    def get(self, request, id=None):
        if id:
            cargo = CargoModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = CargoForm(instance=cargo)
        else:
            form = CargoForm()  # MODO CADASTRO: recebe o formulário vazio
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id})

    def post(self, request):
        if not request.POST['id']:  # CADASTRO NOVO
            id = None
            form = CargoForm(data=request.POST)
        else:  # EDIÇÃO
            id = request.POST['id']
            cargo = CargoModel.objects.get(pk=id)
            form = CargoForm(instance=cargo, data=request.POST)

        if form.is_valid():
            cargo = form.save(commit=False)
            cargo.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id})


def CargoDelete(request, id):
    cargo = CargoModel.objects.get(pk=id)
    cargo.delete()
    return HttpResponseRedirect('/')
