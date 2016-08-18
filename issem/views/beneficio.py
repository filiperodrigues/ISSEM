# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import Beneficio
from issem.forms import BeneficioForm

def add_beneficio(request):
    if request.method == 'POST':
        form = BeneficioForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
        else:
            print (form.errors)
    else:
        form = BeneficioForm
        return render(request, 'cadastro_beneficio.html', {'form': form})

def edita_beneficio(request,id):
    beneficio = Beneficio.objects.get(pk=id)
    if request.method == 'POST':
        form = BeneficioForm(request.POST, instance=beneficio)
        if form.is_valid():
            beneficio = form.save(commit=False)
            beneficio.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = BeneficioForm(instance=beneficio)
        return render(request, 'edita_beneficio.html', {'form': form})

def deleta_beneficio(request, id):
    beneficio = Beneficio.objects.get(pk=id)
    beneficio.delete()
    return HttpResponseRedirect('/')
