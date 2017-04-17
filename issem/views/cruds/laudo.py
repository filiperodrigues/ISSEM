# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import LaudoModel, TipoLaudoModel, ServidorModel, SeguradoModel
from issem.forms import LaudoForm
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


class LaudoView(View):
    template = 'cruds/laudo.html'

    def group_test(user):
        return user.groups.filter(name='Tecnico')

    @method_decorator(user_passes_test(group_test))

    def get(self, request, id=None, id_tipo_laudo=None):
        print('get')
        tipo_laudo = TipoLaudoModel.objects.get(pk=id_tipo_laudo)
        if id:
            laudo = LaudoModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = LaudoForm(instance=laudo)
        else:
            form = LaudoForm()  # MODO CADASTRO: recebe o formulário vazio
        return render(request, self.template, {'form': form, 'tipo_laudo': tipo_laudo.nome, 'method': 'get', 'id': id})

    def post(self, request, id_laudo=None):
        print('oi')
        print(request.POST)
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            print(id)
            laudo = LaudoModel.objects.get(pk=id)
            form = LaudoForm(instance=laudo, data=request.POST)
        else:  # CADASTRO NOVO
            id = None
            form = LaudoForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id})


def LaudoDelete(request, id):
    laudo = LaudoModel.objects.get(pk=id)
    laudo.delete()
    return HttpResponseRedirect('/')
