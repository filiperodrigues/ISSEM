# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import FuncaoModel
from issem.forms import FuncaoForm


def add_funcao(request):
    if request.method == 'POST':
        form = FuncaoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = FuncaoForm()
        return render(request, 'cadastro_funcao.html', {'form': form})


def edita_funcao(request, id):
    funcao = FuncaoModel.objects.get(pk=id)
    if request.method == "POST":
        form = FuncaoForm(request.POST, instance=funcao)
        if form.is_valid():
            funcao = form.save(commit=False)
            funcao.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = FuncaoForm(instance=funcao)
        return render(request, 'edita_funcao.html', {'form': form})


def deleta_funcao(request, id):
    funcao = FuncaoModel.objects.get(pk=id)
    funcao.delete()
    return HttpResponseRedirect('/')
