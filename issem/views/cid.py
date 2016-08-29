# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import CidModel
from issem.forms import CidForm
from django.views.generic.base import View


class CidView(View):
    template = 'cid.html'

    def get(self, request, id=None):
        if id:
            cid = CidModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = CidForm(instance=cid)
        else:
            form = CidForm()  # MODO CADASTRO: recebe o formulário vazio
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id})

    def post(self, request):
        if not request.POST['id']:  # CADASTRO NOVO
            id = None
            form = CidForm(data=request.POST)
        else:  # EDIÇÃO
            id = request.POST['id']
            cid = CidModel.objects.get(pk=id)
            form = CidForm(instance=cid, data=request.POST)

        if form.is_valid():
            cid = form.save(commit=False)
            cid.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id})


def CidDelete(request, id):
    cid = CidModel.objects.get(pk=id)
    cid.delete()
    return HttpResponseRedirect('/')
