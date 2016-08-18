# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import Procedimento_Medico
from issem.forms import Procedimento_MedicoForm


def add_procedimento_medico(request):
    if request.method == 'POST':
        form = Procedimento_MedicoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
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
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = Procedimento_MedicoForm(instance=procedimento_medico)
        return render(request, 'edita_procedimento_medico.html', {'form': form})


def deleta_procedimento_medico(request, id):
    procedimento_medico = Procedimento_Medico.objects.get(pk=id)
    procedimento_medico.delete()
    return HttpResponseRedirect('/')
