# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import TipoLaudoModel
from issem.forms import TipoLaudoForm
from django.views.generic.base import View
from issem.views.pagination import pagination


class TipoLaudoView(View):
    template = 'cruds/tipo_laudo.html'

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


def ListaTiposLaudos(request, msg=None, tipo_msg=None):
    if request.GET or 'page' in request.GET:
        if request.GET.get('filtro'):
            tipos_laudos = TipoLaudoModel.objects.filter(nome__icontains=request.GET.get('filtro'), excluido=0)
        else:
            tipos_laudos = TipoLaudoModel.objects.filter(excluido=False)
    else:
        tipos_laudos = TipoLaudoModel.objects.filter(excluido=False)

    dados, page_range, ultima = pagination(tipos_laudos, request.GET.get('page'))
    return render(request, 'listas/tipos_laudo.html',
                  {'dados': dados, 'page_range': page_range, 'ultima': ultima, 'msg': msg, 'tipo_msg': tipo_msg,
                   'filtro': request.GET.get('filtro')})

def TipoLaudoDelete(request, id):
    tipo_Laudo = TipoLaudoModel.objects.get(pk=id)
    tipo_Laudo.excluido = True
    tipo_Laudo.save()
    return ListaTiposLaudos(request, msg="Tipo de Laudo excluído com sucesso!", tipo_msg="green")