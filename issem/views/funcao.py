# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import FuncaoModel
from issem.forms import FuncaoForm
from django.views.generic.base import View


class FuncaoView(View):
    template = 'funcao.html'

    def get(self, request, id=None):
        if id:
            funcao = FuncaoModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = FuncaoForm(instance=funcao)
        else:
            form = FuncaoForm()  # MODO CADASTRO: recebe o formulário vazio
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id})

    def post(self, request):
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            funcao = FuncaoModel.objects.get(pk=id)
            form = FuncaoForm(instance=funcao, data=request.POST)
        else:  # CADASTRO NOVO
            id = None
            form = FuncaoForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post'})


def FuncaoDelete(request, id):
    funcao = FuncaoModel.objects.get(pk=id)
    funcao.delete()
    return HttpResponseRedirect('/')
