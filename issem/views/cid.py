# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import CidModel
from issem.forms import CidForm
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


class CidView(View):
    template = 'cid.html'

    def group_test(user):
        return user.groups.filter(name='Servidor')

    @method_decorator(user_passes_test(group_test))

    def get(self, request, id=None):
        if id:
            cid = CidModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = CidForm(instance=cid)
        else:
            form = CidForm()  # MODO CADASTRO: recebe o formulário vazio
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id})

    def post(self, request):
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            cid = CidModel.objects.get(pk=id)
            form = CidForm(instance=cid, data=request.POST)
        else:  # CADASTRO NOVO
            id = None
            form = CidForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id})


def CidDelete(request, id):
    cid = CidModel.objects.get(pk=id)
    cid.delete()
    return HttpResponseRedirect('/')

def ApresentaCid(request):
    context_dict = {}
    context_dict['cids'] = CidModel.objects.all()
    return render(request, 'apresenta_cid.html', context_dict)
