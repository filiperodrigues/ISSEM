# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import TipoExameModel
from issem.forms import TipoExameForm
from django.views.generic.base import View


class TipoExameView(View):
    template = 'tipo_exame.html'

    def get(self, request, id=None):
        if id:
            tipo_exame = TipoExameModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = TipoExameForm(instance=tipo_exame)
        else:
            form = TipoExameForm()  # MODO CADASTRO: recebe o formulário vazio
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id})

    def post(self, request):
        if not request.POST['id']:  # CADASTRO NOVO
            id = None
            form = TipoExameForm(data=request.POST)
        else:  # EDIÇÃO
            id = request.POST['id']
            tipo_exame = TipoExameModel.objects.get(pk=id)
            form = TipoExameForm(instance=tipo_exame, data=request.POST)

        if form.is_valid():
            tipo_exame = form.save(commit=False)
            tipo_exame.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post'})


def TipoExameDelete(request, id):
    tipo_exame = TipoExameModel.objects.get(pk=id)
    tipo_exame.delete()
    return HttpResponseRedirect('/')
