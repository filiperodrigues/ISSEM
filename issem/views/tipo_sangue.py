# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import TipoSangueModel
from issem.forms import TipoSangueForm
from django.views.generic.base import View


class TipoSangueView(View):
    template = 'tipo_sangue.html'

    def get(self, request, id=None):
        if id:
            tipo_sangue = TipoSangueModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = TipoSangueForm(instance=tipo_sangue)
        else:
            form = TipoSangueForm()  # MODO CADASTRO: recebe o formulário vazio
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id})

    def post(self, request):
        if not request.POST['id']:  # CADASTRO NOVO
            id = None
            form = TipoSangueForm(data=request.POST)
        else:  # EDIÇÃO
            id = request.POST['id']
            tipo_sangue = TipoSangueModel.objects.get(pk=id)
            form = TipoSangueForm(instance=tipo_sangue, data=request.POST)

        if form.is_valid():
            tipo_sangue = form.save(commit=False)
            tipo_sangue.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id})


def TipoSangueDelete(request, id):
    tipo_sangue = TipoSangueModel.objects.get(pk=id)
    tipo_sangue.delete()
    return HttpResponseRedirect('/')
