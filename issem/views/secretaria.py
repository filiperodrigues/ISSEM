# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import Secretaria
from issem.forms import SecretariaForm


def add_secretaria(request):
    if request.method == 'POST':
        form = SecretariaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = SecretariaForm()
        return render(request, 'cadastro_secretaria.html', {'form': form})


def edita_secretaria(request, id):
    secretaria = Secretaria.objects.get(pk=id)
    if request.method == "POST":
        form = SecretariaForm(request.POST, instance=secretaria)
        if form.is_valid():
            secretaria = form.save(commit=False)
            secretaria.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = SecretariaForm(instance=secretaria)
        return render(request, 'edita_secretaria.html', {'form': form})


def deleta_secretaria(request, id):
    secretaria = Secretaria.objects.get(pk=id)
    secretaria.delete()
    return HttpResponseRedirect('/')
