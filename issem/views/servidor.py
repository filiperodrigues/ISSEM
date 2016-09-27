# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import ServidorModel
from issem.forms import ServidorForm
from django.views.generic.base import View
from issem.models import EstadoModel

class ServidorView(View):
    template = 'servidor.html'

    def get(self, request, id=None):
        if id:
            servidor = ServidorModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = ServidorForm(instance=servidor)
        else:
            form = ServidorForm()  # MODO CADASTRO: recebe o formulário vazio
        estados = EstadoModel.objects.all()
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id, 'estados': estados})

    def post(self, request):
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            servidor = ServidorModel.objects.get(pk=id)
            form = ServidorForm(instance=servidor, data=request.POST)
        else:  # CADASTRO NOVO
            # id = None
            form = ServidorForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post'})


def ServidorDelete(request, id):
    servidor = ServidorModel.objects.get(pk=id)
    servidor.delete()
    return HttpResponseRedirect('/')


def ApresentaServidor(request):
    context_dict = {}
    context_dict['servidores'] = ServidorModel.objects.all()
    return render(request, 'servidores.html', context_dict)
