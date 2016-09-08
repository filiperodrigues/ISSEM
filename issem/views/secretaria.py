# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import SecretariaModel
from issem.forms import SecretariaForm
from django.views.generic.base import View


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
        if not request.POST['id']:  # CADASTRO NOVO
            id = None
            form = SecretariaForm(data=request.POST)
        else:  # EDIÇÃO
            id = request.POST['id']
            secretaria = SecretariaModel.objects.get(pk=id)
            form = SecretariaForm(instance=secretaria, data=request.POST)

        if form.is_valid():
            secretaria = form.save(commit=False)
            secretaria.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post'})


def SecretariaDelete(request, id):
    secretaria = SecretariaModel.objects.get(pk=id)
    secretaria.delete()
    return HttpResponseRedirect('/')
