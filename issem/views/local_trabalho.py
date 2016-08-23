# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import Local_Trabalho
from issem.forms import Local_TrabalhoForm


def add_local_trabalho(request):
    if request.method == 'POST':
        print "COM POST"
        form = Local_TrabalhoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
        else:
            print "DEU MERDA"
            print(form.errors)
    else:
        print "SEM POST"
        form = Local_TrabalhoForm()
        return render(request, 'cadastro_local_trabalho.html', {'form': form})


def edita_local_trabalho(request, id):
    local_trabalho = Local_Trabalho.objects.get(pk=id)
    if request.method == "POST":
        form = Local_TrabalhoForm(request.POST, instance=local_trabalho)
        if form.is_valid():
            local_trabalho = form.save(commit=False)
            local_trabalho.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = Local_TrabalhoForm(instance=local_trabalho)
        return render(request, 'edita_local_trabalho.html', {'form': form})


def deleta_local_trabalho(request, id):
    local_trabalho = Local_Trabalho.objects.get(pk=id)
    local_trabalho.delete()
    return HttpResponseRedirect('/')
