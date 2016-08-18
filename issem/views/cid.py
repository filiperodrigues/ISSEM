# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import Cid
from issem.forms import CidForm


def add_cid(request):
    if request.method == 'POST':
        form = CidForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
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
            return HttpResponseRedirect('/')
        else:
            print(form.errors)
    else:
        form = CidForm(instance=cid)
        return render(request, 'edita_cid.html', {'form': form})


def deleta_cid(request, id):
    cid = Cid.objects.get(pk=id)
    cid.delete()
    return HttpResponseRedirect('/')
