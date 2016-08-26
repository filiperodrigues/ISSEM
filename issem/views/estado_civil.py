# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import EstadoCivilModel
from issem.forms import EstadoCivilForm


def add_estado_civil(request):
    if request.method == 'POST':
        form = EstadoCivilForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = EstadoCivilForm()
        return render(request, 'cadastro_estado_civil.html', {'form': form})


def edita_estado_civil(request, id):
    tipo_estado_civil = EstadoCivilModel.objects.get(pk=id)
    if request.method == "POST":
        form = EstadoCivilForm(request.POST, instance=tipo_estado_civil)
        if form.is_valid():
            estado_civil = form.save(commit=False)
            estado_civil.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = EstadoCivilForm(instance=tipo_estado_civil)
        return render(request, 'edita_estado_civil.html', {'form': form})


def deleta_estado_civil(request, id):
    estado_civil = EstadoCivilModel.objects.get(pk=id)
    estado_civil.delete()
    return HttpResponseRedirect('/')