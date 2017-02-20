# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import TipoLaudoModel
from issem.forms import TipoLaudoForm
from django.views.generic.base import View


class TipoLaudoView(View):
    template = 'tipo_laudo.html'

    def get(self, request, id=None):
        if id:
            tipo_Laudo = TipoLaudoModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = TipoLaudoForm(instance=tipo_Laudo)
        else:
            form = TipoLaudoForm()  # MODO CADASTRO: recebe o formulário vazio
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id})

    def post(self, request):
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            tipo_Laudo = TipoLaudoModel.objects.get(pk=id)
            form = TipoLaudoForm(instance=tipo_Laudo, data=request.POST)
        else:  # CADASTRO NOVO
            id = None
            form = TipoLaudoForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id})


def ListaTiposLaudos(request):
    context_dict = {}
    context_dict['tipos_laudos'] = TipoLaudoModel.objects.all()
    return render(request, 'tipos_laudos.html', context_dict)


def TipoLaudoDelete(request, id):
    tipo_Laudo = TipoLaudoModel.objects.get(pk=id)
    tipo_Laudo.delete()
    return HttpResponseRedirect('/')