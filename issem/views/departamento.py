# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import DepartamentoModel
from issem.forms import DepartamentoForm
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator

class DepartamentoView(View):
    template = 'departamento.html'

    def group_test(user):
        return user.groups.filter(name='Servidor')

    @method_decorator(user_passes_test(group_test))

    def get(self, request, id=None):
        if id:
            departamento = DepartamentoModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = DepartamentoForm(instance=departamento)
        else:
            form = DepartamentoForm()  # MODO CADASTRO: recebe o formulário vazio
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id})

    def post(self, request):
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            departamento = DepartamentoModel.objects.get(pk=id)
            form = DepartamentoForm(instance=departamento, data=request.POST)
        else:  # CADASTRO NOVO
            id = None
            form = DepartamentoForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id})


def DepartamentoDelete(request, id):
    departamento = DepartamentoModel.objects.get(pk=id)
    departamento.delete()
    return HttpResponseRedirect('/')
