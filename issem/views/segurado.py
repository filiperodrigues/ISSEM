# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import SeguradoModel
from issem.forms import SeguradoForm
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group
from issem.views.pagination import pagination


class SeguradoView(View):
    template = 'segurado.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    @method_decorator(user_passes_test(group_test))

    def get(self, request, id=None):
        if id:
            segurado = SeguradoModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = SeguradoForm(instance=segurado)
        else:
            form = SeguradoForm()  # MODO CADASTRO: recebe o formulário vazio
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id})

    def post(self, request):
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            segurado = SeguradoModel.objects.get(pk=id)
            form = SeguradoForm(instance=segurado, data=request.POST)
        else:  # CADASTRO NOVO
            id = None
            form = SeguradoForm(data=request.POST)

        if form.is_valid():
            form.save()

            gp = Group.objects.get(name='Segurado')
            user = SeguradoModel.objects.get(username=request.POST["username"])
            user.groups.add(gp)
            user.save()
            return render(request, 'blocos/mensagem_cadastro_concluido_segurado.html', {'id_segurado': user.id})
            # return render(request, 'blocos/mensagem_cadastro_concluido_segurado.html')

        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id})


def SeguradoDelete(request, id):
    segurado = SeguradoModel.objects.get(pk=id)
    segurado.delete()
    return HttpResponseRedirect('/')


def ListaSegurados(request):
    segurados = SeguradoModel.objects.all()
    dados = pagination(segurados, request.GET.get('page'))
    return render(request, 'segurados.html', {'dados': dados})