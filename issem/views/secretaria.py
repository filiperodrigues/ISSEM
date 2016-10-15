# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from issem.models import SecretariaModel
from issem.forms import SecretariaForm
from django.views.generic.base import View
from django.core import serializers


class SecretariaView(View):
    template = 'secretaria.html'

    def get(self, request, id=None):
        if id:
            secretaria = SecretariaModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = SecretariaForm(instance=secretaria)
        else:
            form = SecretariaForm()  # MODO CADASTRO: recebe o formulário vazio
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id})

    def post(self, request):
        if 'sec' in request.POST:
            nome = request.POST['sec']
            nome_sec = SecretariaModel(nome=nome)
            nome_sec.save()
            nome_sec = SecretariaModel.objects.all()
            json = serializers.serialize("json", nome_sec)
            return HttpResponse(json)

        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            secretaria = SecretariaModel.objects.get(pk=id)
            form = SecretariaForm(instance=secretaria, data=request.POST)
        else:  # CADASTRO NOVO
            id = None
            form = SecretariaForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id})


def SecretariaDelete(request, id):
    secretaria = SecretariaModel.objects.get(pk=id)
    secretaria.delete()
    return HttpResponseRedirect('/')
