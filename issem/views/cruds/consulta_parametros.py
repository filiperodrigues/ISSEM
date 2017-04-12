# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import ConsultaParametrosModel
from issem.forms import ConsultaParametrosForm
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


class ConstultaParametrosView(View):
    template = 'cruds/consulta_parametros.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    @method_decorator(user_passes_test(group_test))

    def get(self, request, id=None):
        if id:
            consulta_parametros = ConsultaParametrosModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = ConsultaParametrosForm(instance=consulta_parametros)
        else:
            form = ConsultaParametrosForm()  # MODO CADASTRO: recebe o formulário vazio
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id})

    def post(self, request):
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            consulta_parametros = ConsultaParametrosModel.objects.get(pk=id)
            form = ConsultaParametrosForm(instance=consulta_parametros, data=request.POST)
        else:  # CADASTRO NOVO
            id = None
            form = ConsultaParametrosForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id})


def ConsultaParametrosDelete(request, id):
    consulta_parametros = ConsultaParametrosModel.objects.get(pk=id)
    consulta_parametros.delete()
    return HttpResponseRedirect('/')
