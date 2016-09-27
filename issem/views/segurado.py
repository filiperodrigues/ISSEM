# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import SeguradoModel
from issem.forms import SeguradoForm
from django.views.generic.base import View
from issem.models import EstadoModel


class SeguradoView(View):
    template = 'segurado.html'

    def get(self, request, id=None):
        if id:
            segurado = SeguradoModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = SeguradoForm(instance=segurado)
        else:
            form = SeguradoForm()  # MODO CADASTRO: recebe o formulário vazio
        estados = EstadoModel.objects.all()
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id, 'estados': estados})

    def post(self, request):
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            segurado = SeguradoModel.objects.get(pk=id)
            form = SeguradoForm(instance=segurado, data=request.POST)
        else:  # CADASTRO NOVO
            id = None
            form = SeguradoForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post'})


def SeguradoDelete(request, id):
    segurado = SeguradoModel.objects.get(pk=id)
    segurado.delete()
    return HttpResponseRedirect('/')

def ApresentaSegurado(request):
    context_dict = {}
    context_dict['segurados'] = SeguradoModel.objects.all()
    return render(request, 'segurados.html', context_dict)
