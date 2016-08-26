# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models.servidor import Servidor
from issem.forms.servidor import ServidorForm


def add_servidor(request):
    if request.method == 'POST':
        form = ServidorForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = ServidorForm()
        return render(request, 'cadastro_servidor.html', {'form': form})


def edita_servidor(request, id):
    servidor = Servidor.objects.get(pk=id)
    if request.method == "POST":
        form = ServidorForm(request.POST, instance=servidor)
        if form.is_valid():
            servidor = form.save(commit=False)
            servidor.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = ServidorForm(instance=servidor)
        return render(request, 'edita_servidor.html', {'form': form})


def deleta_servidor(request, id):
    servidor = Servidor.objects.get(pk=id)
    servidor.delete()
    return HttpResponseRedirect('/')

def apresenta_servidor(request):
    context_dict = {}
    context_dict['servidores'] = Servidor.objects.all()
    return render(request, 'servidores.html', context_dict)
