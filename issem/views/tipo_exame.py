# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import Tipo_Exame
from issem.forms import Tipo_ExameForm


def add_tipo_exame(request):
    if request.method == 'POST':
        form = Tipo_ExameForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = Tipo_ExameForm()
        return render(request, 'cadastro_tipo_exame.html', {'form': form})


def edita_tipo_exame(request, id):
    tipo_exame = Tipo_Exame.objects.get(pk=id)
    if request.method == "POST":
        form = Tipo_ExameForm(request.POST, instance=tipo_exame)
        if form.is_valid():
            tipo_exame = form.save(commit=False)
            tipo_exame.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = Tipo_ExameForm(instance=tipo_exame)
        return render(request, 'edita_tipo_exame.html', {'form': form})


def deleta_tipo_exame(request, id):
    tipo_exame = Tipo_Exame.objects.get(pk=id)
    tipo_exame.delete()
    return HttpResponseRedirect('/')