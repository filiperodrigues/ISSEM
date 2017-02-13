# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import DependenteModel, SeguradoModel
from issem.forms import DependenteForm, SeguradoForm
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


class DependenteView(View):
    template = 'dependente.html'

    def group_test(user):
        return user.groups.filter(name='Servidor')

    @method_decorator(user_passes_test(group_test))

    def get(self, request, id=None, id_segurado=None):
        if id:
            dependente = DependenteModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = DependenteForm(instance=dependente)
        else:
            form = DependenteForm()  # MODO CADASTRO: recebe o formulário vazio
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id, 'id_segurado': id_segurado})

    def post(self, request, id_segurado=None):
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            dependente = DependenteModel.objects.get(pk=id)
            form = DependenteForm(instance=dependente, data=request.POST)
        else:  # CADASTRO NOVO
            id = None
            form = DependenteForm(data=request.POST)

        if form.is_valid():
            form.save()
            if id_segurado != None:
                dependente_current = DependenteModel.objects.get(username=request.POST["username"])
                segurado = SeguradoModel.objects.get(pk=id_segurado)
                segurado.dependente = dependente_current
                # form_segurado = SeguradoForm(instance=segurado, data=request.POST)
                # print(form_segurado)
                # obj = form_segurado.cleaned_data
                # obj = form_segurado.save(commit=False)
                # obj.dependente = segurado
                # obj.save()
                # form.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id, 'id_segurado': id_segurado})

def ListaDependentes(request):
    context_dict = {}
    context_dict['dependentes'] = DependenteModel.objects.all()
    return render(request, 'dependentes.html', context_dict)


def DependenteDelete(request, id):
    dependente = DependenteModel.objects.get(pk=id)
    dependente.delete()
    return HttpResponseRedirect('/')
