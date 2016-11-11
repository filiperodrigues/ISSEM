# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import DependenteModel
from issem.forms import DependenteForm
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


class DependenteView(View):
    template = 'dependente.html'

    def group_test(user):
        return user.groups.filter(name='Servidor')

    @method_decorator(user_passes_test(group_test))

    def get(self, request, id=None):
        if id:
            dependente = DependenteModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = DependenteForm(instance=dependente)
        else:
            form = DependenteForm()  # MODO CADASTRO: recebe o formulário vazio
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id})

    def post(self, request):
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            dependente = DependenteModel.objects.get(pk=id)
            form = DependenteForm(instance=dependente, data=request.POST)
        else:  # CADASTRO NOVO
            id = None
            form = DependenteForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id})


def DependenteDelete(request, id):
    dependente = DependenteModel.objects.get(pk=id)
    dependente.delete()
    return HttpResponseRedirect('/')
