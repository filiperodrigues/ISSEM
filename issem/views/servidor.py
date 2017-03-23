# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import ServidorModel
from issem.forms import ServidorFormCad
from django.views.generic.base import View
from issem.models import EstadoModel
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group
from issem.views.pagination import pagination


class ServidorView(View):
    template = 'servidor.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    @method_decorator(user_passes_test(group_test))

    def get(self, request, id=None):
        group_user = False
        if id:  # EDIÇÃO
            servidor = ServidorModel.objects.get(pk=id)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            form = ServidorFormCad(instance=servidor)
            group_user = Group.objects.get(user=id).id
        else:  # CADASTRO NOVO
            form = ServidorFormCad()  # MODO CADASTRO: recebe o formulário vazio
        return render(request, self.template, {'form': form, 'method': 'get', 'id': id, 'group_user': group_user})

    def post(self, request):
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            servidor = ServidorModel.objects.get(pk=id)
            form = ServidorFormCad(instance=servidor, data=request.POST)
        else:  # CADASTRO NOVO
            id = None
            form = ServidorFormCad(data=request.POST)

        if form.is_valid():
            form.save()
            if (id != None):
                if Group.objects.get(user=id):
                    group_name = Group.objects.get(user=id)
                    group_name.user_set.remove(id)

            gp = Group.objects.get(id=request.POST["groups"])
            user = ServidorModel.objects.get(username=request.POST["username"])
            user.groups.add(gp)

            user.save()

            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id})


def ServidorDelete(request, id):
    servidor = ServidorModel.objects.get(pk=id)
    servidor.delete()
    return HttpResponseRedirect('/')


def ListaServidores(request):
    servidores = ServidorModel.objects.all()
    dados, page_range, ultima = pagination(servidores, request.GET.get('page'))
    return render(request, 'servidores.html', {'dados': dados, 'page_range': page_range, 'ultima' : ultima})