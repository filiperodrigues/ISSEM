#coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from issem.models import Departamento, Cid, Procedimento_Medico, Beneficio, Funcao, Cargo
from issem.forms import DepartamentoForm, CidForm, Procedimento_MedicoForm, BeneficioForm, FuncaoForm, CargoForm

def index(request):
    departamentos = Departamento.objects.all()
    cids = Cid.objects.all()
    procedimentos_medicos = Procedimento_Medico.objects.all()
    beneficios = Beneficio.objects.all()
    funcoes = Funcao.objects.all()
    cargos = Cargo.objects.all()
    context_dict = {'departamentos': departamentos, 'cids': cids, 'procedimentos_medicos': procedimentos_medicos, 'beneficios': beneficios, 'funcoes': funcoes, 'cargos': cargos}
    return render(request, 'index.html', context_dict)

## DEPARTAMENTO ##
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
        return render(request, 'cadastro_departamento.html', {'form': form})

def edita_departamento(request, id):
    departamento = Departamento.objects.get(pk=id)
    if request.method == "POST":
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            departamento = form.save(commit=False)
            departamento.save()
            return index(request)
        else:
            print(form.errors)
    else:
        form = DepartamentoForm(instance=departamento)
        return render(request, 'edita_departamento.html', {'form': form})

def deleta_departamento(request, id):
    departamento = Departamento.objects.get(pk=id)
    departamento.delete()
    return index(request)

## CID ##
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
        return render(request, 'cadastro_cid.html', {'form': form})


def edita_cid(request, id):
    cid = Cid.objects.get(pk=id)
    if request.method == "POST":
        form = CidForm(request.POST, instance=cid)
        if form.is_valid():
            cid = form.save(commit=False)
            cid.save()
            return index(request)
        else:
            print(form.errors)
    else:
        form = CidForm(instance=cid)
        return render(request, 'edita_cid.html', {'form': form})

def deleta_cid(request, id):
    cid = Cid.objects.get(pk=id)
    cid.delete()
    return index(request)

## PROCEDIMENTO MÉDICO ##
def add_procedimento_medico(request):
    if request.method == 'POST':
        form = Procedimento_MedicoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    else:
        form = Procedimento_MedicoForm()
        return render(request, 'cadastro_procedimento_medico.html', {'form': form})

def edita_procedimento_medico(request,id):
    procedimento_medico = Procedimento_Medico.objects.get(pk=id)
    if request.method == 'POST':
        form = Procedimento_MedicoForm(request.POST, instance=procedimento_medico)
        if form.is_valid():
            procedimento_medico = form.save(commit=False)
            procedimento_medico.save()
            return index(request)
        else:
            print(form.errors)
    else:
        form = Procedimento_MedicoForm(instance=procedimento_medico)
        return render(request, 'edita_procedimento_medico.html', {'form': form})

def deleta_procedimento_medico(request, id):
    procedimento_medico = Procedimento_Medico.objects.get(pk=id)
    procedimento_medico.delete()
    return index(request)

## BENEFÍCIOS ##
def add_beneficio(request):
    if request.method == 'POST':
        form = BeneficioForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
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
            return index(request)
        else:
            print(form.errors)
    else:
        form = BeneficioForm(instance=beneficio)
        return render(request, 'edita_beneficio.html', {'form': form})

def deleta_beneficio(request, id):
    beneficio = Beneficio.objects.get(pk=id)
    beneficio.delete()
    return index(request)

## FUNÇÃO ##
def add_funcao(request):
    if request.method == 'POST':
        form = FuncaoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    else:
        form = FuncaoForm()
        return render(request, 'cadastro_funcao.html', {'form': form})

def edita_funcao(request, id):
    funcao = Funcao.objects.get(pk=id)
    if request.method == "POST":
        form = FuncaoForm(request.POST, instance=funcao)
        if form.is_valid():
            funcao = form.save(commit=False)
            funcao.save()
            return index(request)
        else:
            print(form.errors)
    else:
        form = FuncaoForm(instance=funcao)
        return render(request, 'edita_funcao.html', {'form': form})

def deleta_funcao(request, id):
    funcao = Funcao.objects.get(pk=id)
    funcao.delete()
    return index(request)


## CARGO ##

def add_cargo(request):
    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    else:
        form = FuncaoForm()
        return render(request, 'cadastro_cargo.html', {'form': form})

def edita_cargo(request, id):
    cargo = Cargo.objects.get(pk=id)
    if request.method == "POST":
        form = CargoForm(request.POST, instance=cargo)
        if form.is_valid():
            cargo = form.save(commit=False)
            cargo.save()
            return index(request)
        else:
            print(form.errors)
    else:
        form = CargoForm(instance=cargo)
        return render(request, 'edita_cargo.html', {'form': form})

def deleta_cargo(request, id):
    cargo = Cargo.objects.get(pk=id)
    cargo.delete()
    return index(request)