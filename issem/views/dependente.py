# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models.dependente import Dependente
from issem.forms.dependente import DependenteForm
#from issem.views import index


def add_dependente(request):
    if request.method == 'POST':
        form = DependenteForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = DependenteForm()
        return render(request, 'cadastro_dependente.html', {'form': form})


def edita_dependente(request, id):
    dependente = Dependente.objects.get(pk=id)
    if request.method == "POST":
        form = DependenteForm(request.POST, instance=dependente)
        if form.is_valid():
            dependente = form.save(commit=False)
            dependente.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = DependenteForm(instance=dependente)
        return render(request, 'edita_dependente.html', {'form': form})


def deleta_dependente(request, id):
    dependente = Dependente.objects.get(pk=id)
    dependente.delete()
    return HttpResponseRedirect('/')
