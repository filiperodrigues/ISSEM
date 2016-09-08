# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import TipoSanguineoModel
from issem.forms import TipoSanguineoForm
from django.views.generic.base import View


class TipoSanguineoView(View):
    template = 'tipo_sanguineo.html'

    def get(self, request, id=None):
        if id:
            tipo_sanguineo = TipoSanguineoModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = TipoSanguineoForm(instance=tipo_sanguineo)
        else:
            form = TipoSanguineoForm()  # MODO CADASTRO: recebe o formulário vazio
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id})

    def post(self, request):
        if not request.POST['id']:  # CADASTRO NOVO
            id = None
            form = TipoSanguineoForm(data=request.POST)
        else:  # EDIÇÃO
            id = request.POST['id']
            tipo_sanguineo = TipoSanguineoModel.objects.get(pk=id)
            form = TipoSanguineoForm(instance=tipo_sanguineo, data=request.POST)

        if form.is_valid():
            tipo_sanguineo = form.save(commit=False)
            tipo_sanguineo.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post'})


def TipoSanguineoDelete(request, id):
    tipo_sanguineo = TipoSanguineoModel.objects.get(pk=id)
    tipo_sanguineo.delete()
    return HttpResponseRedirect('/')
