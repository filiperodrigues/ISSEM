# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import TipoLaudoModel
from issem.forms import TipoLaudoForm
from django.views.generic.base import View
from issem.views.pagination import pagination


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
    tipo_laudos = TipoLaudoModel.objects.filter(excluido=0)
    dados, page_range, ultima = pagination(tipo_laudos, request.GET.get('page'))
    return render(request, 'tipos_laudos.html', {'dados': dados, 'page_range':page_range, 'ultima' : ultima})


def TipoLaudoDelete(request, id):
    tipo_Laudo = TipoLaudoModel.objects.get(pk=id)
    tipo_Laudo.excluido = True
    tipo_Laudo.save()
    return HttpResponseRedirect('/')
