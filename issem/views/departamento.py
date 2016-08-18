# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import Departamento
from issem.forms import DepartamentoForm
from issem.views import index


def add_departamento(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = DepartamentoForm()
        return render(request, 'cadastro_departamento.html', {'form': form})


def edita_departamento(request, id):
    departamento = Departamento.objects.get(pk=id)
    if request.method == "POST":
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            departamento = form.save(commit=False)
            departamento.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = DepartamentoForm(instance=departamento)
        return render(request, 'edita_departamento.html', {'form': form})


def deleta_departamento(request, id):
    departamento = Departamento.objects.get(pk=id)
    departamento.delete()
    return HttpResponseRedirect('/')