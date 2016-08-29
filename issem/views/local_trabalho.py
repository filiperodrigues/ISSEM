# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import LocalTrabalhoModel
from issem.forms import LocalTrabalhoForm


def add_local_trabalho(request):
    if request.method == 'POST':
        #print "COM POST"
        form = LocalTrabalhoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')

    else:
        #print "SEM POST"
        form = LocalTrabalhoForm()
        return render(request, 'cadastro_local_trabalho.html', {'form': form})


def edita_local_trabalho(request, id):
    local_trabalho = LocalTrabalhoModel.objects.get(pk=id)
    if request.method == "POST":
        form = LocalTrabalhoForm(request.POST, instance=local_trabalho)
        if form.is_valid():
            local_trabalho = form.save(commit=False)
            local_trabalho.save()
            return HttpResponseRedirect('/')

    else:
        form = LocalTrabalhoForm(instance=local_trabalho)
        return render(request, 'edita_local_trabalho.html', {'form': form})


def deleta_local_trabalho(request, id):
    local_trabalho = LocalTrabalhoModel.objects.get(pk=id)
    local_trabalho.delete()
    return HttpResponseRedirect('/')
