# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import TipoDependenteModel
from issem.forms import TipoDependenteForm


def add_tipo_dependente(request):
    if request.method == 'POST':
        form = TipoDependenteForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = TipoDependenteForm()
        return render(request, 'cadastro_tipo_dependente.html', {'form': form})


def edita_tipo_dependente(request, id):
    tipo_dependente = TipoDependenteModel.objects.get(pk=id)
    if request.method == "POST":
        form = TipoDependenteForm(request.POST, instance=tipo_dependente)
        if form.is_valid():
            tipo_dependente = form.save(commit=False)
            tipo_dependente.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = TipoDependenteForm(instance=tipo_dependente)
        return render(request, 'edita_tipo_dependente.html', {'form': form})


def deleta_tipo_dependente(request, id):
    tipo_dependente = TipoDependenteModel.objects.get(pk=id)
    tipo_dependente.delete()
    return HttpResponseRedirect('/')
