from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from issem.models import Departamento, Cid, Procedimento_Medico, Beneficios
from issem.forms import DepartamentoForm, CidForm, Procedimento_MedicoForm, BeneficiosForm


def index(request):
    departamento = Departamento.objects.all()
    cid = Cid.objects.all()
    procedimento_medico = Procedimento_Medico.objects.all()
    beneficios = Beneficios.objects.all()
    context_dict = {'departamento': departamento, 'cid':cid, 'procedimento_medico': procedimento_medico, 'beneficios':beneficios}
    return render(request, 'issem/index.html', context_dict)

##DEPARTAMENTOS##
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

def edita_departamento(request, id):
    departamento = Departamento.objects.get(pk=id)
    if request.method == "POST":
        form = DepartamentoForm(request.POST, instance=departamento)

def delete_departamento(request, id):
    b = Departamento.objects.get(pk=id)
    b.delete()
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
    return render(request, 'issem/cadastro_cid.html', {'form': form})

def edita_cid(request, id):
    cid = Cid.objects.get(pk=id)
    if request.method == "POST":
        form = CidForm(request.POST, instance=cid)

def delete_cid(request, id):
    b = Cid.objects.get(pk=id)
    b.delete()
    return index(request)

#PROCEDIMENTO MÉDICO
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
    return render(request, 'issem/cadastro_procedimento_medico.html', {'form': form})

def edit_procedimento_medico(request,id):
    procedimento_medico = Procedimento_Medico.objects.get(pk=id)
    if request.method == 'POST':
        form = Procedimento_MedicoForm(request.POST, instance=procedimento_medico)
        if form.is_valid():
            procedimento_medicoos = form.save(commit=False)
            procedimento_medico.save()
            return index(request)
    else:
        form = Procedimento_MedicoForm(instance=procedimento_medico)
        return render(request, 'issem/editar_procedimento_medico.html', {'form': form})

def delete_procedimento_medico(request, id):
    procedimento_medico = Procedimento_Medico.objects.get(pk=id)
    procedimento_medico.delete()
    return index(request)

##BENEFICIOS##
def add_beneficios(request):
    if request.method == 'POST':
        form = BeneficiosForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print (form.errors)
    else:
        form = BeneficiosForm
    return render(request, 'issem/cadastro_beneficios.html', {'form': form})

def edit_beneficios(request,id):
    beneficios = Beneficios.objects.get(pk=id)
    if request.method == 'POST':
        form = BeneficiosForm(request.POST, instance=beneficios)
        if form.is_valid():
            beneficios = form.save(commit=False)
            beneficios.save()
            return index(request)
    else:
        form = BeneficiosForm(instance=beneficios)
        return render(request, 'issem/editar_beneficios.html', {'form': form})

def delete_beneficios(request, id):
    beneficios = Beneficios.objects.get(pk=id)
    beneficios.delete()
    return index(request)