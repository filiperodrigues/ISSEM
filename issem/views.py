#coding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import Departamento, Cid
from issem.forms import DepartamentoForm, CidForm
from django.http import HttpResponse

def index(request):
    departamento = Departamento.objects.all()
    cid = Cid.objects.all()
    context_dict = {'departamento': departamento, 'cid':cid}
    return render(request, 'issem/index.html', context_dict)

def add_departamento(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    else:
        form = DepartamentoForm()
    return render(request, 'issem/cadastro_departamento.html', {'form': form})

def add_cid(request):
    if request.method == 'POST':
        form = CidForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    else:
        form = CidForm()
    return render(request, 'issem/cadastro_cid.html', {'form': form})

def delete_cid(request, id):
    b = Cid.objects.get(pk=id)
    b.delete()
    return index(request)

def edita_cid(request, id):
    cid = Cid.objects.get(pk=id)
    if request.method == "POST":
        form = CidForm(request.POST, instance=cid)
        if form.is_valid():
            cid = form.save(commit=False)
            cid.save()
            return index(request)

    else:

        form = CidForm(instance=cid)
        return render(request, 'issem/editar_cid.html', {'form': form})
