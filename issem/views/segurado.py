# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models.segurado import Segurado
from issem.forms.segurado import SeguradoForm


def add_segurado(request):
    if request.method == 'POST':
        form = SeguradoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = SeguradoForm()
        return render(request, 'cadastro_segurado.html', {'form': form})


def edita_segurado(request, id):
    segurado = Segurado.objects.get(pk=id)
    if request.method == "POST":
        form = SeguradoForm(request.POST, instance=segurado)
        if form.is_valid():
            segurado = form.save(commit=False)
            segurado.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = SeguradoForm(instance=segurado)
        return render(request, 'edita_segurado.html', {'form': form})


def deleta_segurado(request, id):
    segurado = Segurado.objects.get(pk=id)
    segurado.delete()
    return HttpResponseRedirect('/')
