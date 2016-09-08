# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import LocalTrabalhoModel
from issem.forms import LocalTrabalhoForm
from django.views.generic.base import View


class LocalTrabalhoView(View):
    template = 'local_trabalho.html'

    def get(self, request, id=None):
        if id:
            local_trabalho = LocalTrabalhoModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = LocalTrabalhoForm(instance=local_trabalho)
        else:
            form = LocalTrabalhoForm()  # MODO CADASTRO: recebe o formulário vazio
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id})

    def post(self, request):
        if not request.POST['id']:  # CADASTRO NOVO
            id = None
            form = LocalTrabalhoForm(data=request.POST)
        else:  # EDIÇÃO
            id = request.POST['id']
            local_trabalho = LocalTrabalhoModel.objects.get(pk=id)
            form = LocalTrabalhoForm(instance=local_trabalho, data=request.POST)

        if form.is_valid():
            local_trabalho = form.save(commit=False)
            local_trabalho.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post'})


def LocalTrabalhoDelete(request, id):
    local_trabalho = LocalTrabalhoModel.objects.get(pk=id)
    local_trabalho.delete()
    return HttpResponseRedirect('/')
