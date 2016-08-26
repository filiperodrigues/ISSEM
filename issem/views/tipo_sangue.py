# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import TipoSangueModel
from issem.forms import TipoSangueForm


def add_tipo_sangue(request):
    if request.method == 'POST':
        form = TipoSangueForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = TipoSangueForm()
        return render(request, 'cadastro_tipo_sangue.html', {'form': form})


def edita_tipo_sangue(request, id):
    tipo_sangue = TipoSangueModel.objects.get(pk=id)
    if request.method == "POST":
        form = TipoSangueForm(request.POST, instance=tipo_sangue)
        if form.is_valid():
            tipo_sangue = form.save(commit=False)
            tipo_sangue.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = TipoSangueForm(instance=tipo_sangue)
        return render(request, 'edita_tipo_sangue.html', {'form': form})


def deleta_tipo_sangue(request, id):
    tipo_sangue = TipoSangueModel.objects.get(pk=id)
    tipo_sangue.delete()
    return HttpResponseRedirect('/')
