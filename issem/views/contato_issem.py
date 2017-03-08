# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import ContatoIssemModel
from issem.forms import ContatoIssemForm
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


class ContatoIssemView(View):
    template = 'contato_issem.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    @method_decorator(user_passes_test(group_test))

    def get(self, request, id=None):
        if id:
            contato_issem = ContatoIssemModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = ContatoIssemForm(instance=contato_issem)
        else:
            form = ContatoIssemForm()  # MODO CADASTRO: recebe o formulário vazio
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id})

    def post(self, request):
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            contato_issem = ContatoIssemModel.objects.get(pk=id)
            form = ContatoIssemForm(instance=contato_issem, data=request.POST)
        else:  # CADASTRO NOVO
            id = None
            form = ContatoIssemForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id})


def ContatoIssemDelete(request, id):
    contato_issem = ContatoIssemModel.objects.get(pk=id)
    contato_issem.delete()
    return HttpResponseRedirect('/')


def ListaContatosIssem(request):
    context_dict = {}
    context_dict['contatos'] = ContatoIssemModel.objects.all()
    context_dict['model'] = "contato_issem"
    return render(request, 'contatos_issem.html', context_dict)
