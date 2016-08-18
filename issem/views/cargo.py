# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import Cargo
from issem.forms import CargoForm


def add_cargo(request):
    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = CargoForm()
        return render(request, 'cadastro_cargo.html', {'form': form})


def edita_cargo(request, id):
    cargo = Cargo.objects.get(pk=id)
    if request.method == "POST":
        form = CargoForm(request.POST, instance=cargo)
        if form.is_valid():
            cargo = form.save(commit=False)
            cargo.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = CargoForm(instance=cargo)
        return render(request, 'edita_cargo.html', {'form': form})


def deleta_cargo(request, id):
    cargo = Cargo.objects.get(pk=id)
    cargo.delete()
    return HttpResponseRedirect('/')
