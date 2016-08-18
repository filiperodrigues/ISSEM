# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import Tipo_Dependente
from issem.forms import Tipo_DependenteForm


def add_tipo_dependente(request):
    if request.method == 'POST':
        form = Tipo_DependenteForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = Tipo_DependenteForm()
        return render(request, 'cadastro_tipo_dependente.html', {'form': form})


def edita_tipo_dependente(request, id):
    tipo_dependente = Tipo_Dependente.objects.get(pk=id)
    if request.method == "POST":
        form = Tipo_DependenteForm(request.POST, instance=tipo_dependente)
        if form.is_valid():
            tipo_dependente = form.save(commit=False)
            tipo_dependente.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = Tipo_DependenteForm(instance=tipo_dependente)
        return render(request, 'edita_tipo_dependente.html', {'form': form})


def deleta_tipo_dependente(request, id):
    tipo_dependente = Tipo_Dependente.objects.get(pk=id)
    tipo_dependente.delete()
    return HttpResponseRedirect('/')
