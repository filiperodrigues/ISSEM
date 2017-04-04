# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from issem.models import ServidorModel
from issem.forms import ServidorFormCad, PessoaPasswordForm, ServidorFormEdit
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
            form = ServidorFormEdit(instance=servidor)
            group_user = Group.objects.get(user=id)
            id_group_user = group_user.id
        else:  # CADASTRO NOVO
            form = ServidorFormCad()  # MODO CADASTRO: recebe o formulário vazio
            id_group_user = ""

        return render(request, self.template, {'form': form, 'method': 'get', 'id': id, 'group_user': group_user, 'id_group_user' : id_group_user})
        # return render(request, self.template, {'form': form, 'method': 'get', 'id': id})

    def post(self, request, id=None):
        id_group_user = 0
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            servidor = ServidorModel.objects.get(pk=id)
            form = ServidorFormEdit(instance=servidor, data=request.POST)
            group_user = Group.objects.get(user=id)
            id_group_user = group_user.id

            if form.is_valid():
                form.save()
                msg = 'Alterações realizadas com sucesso!'
                tipo_msg = 'green'
            else:
                print(form.errors)
                msg = 'Erros encontrados!'
                tipo_msg = 'red'

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
                msg = 'Cadastro efetuado com sucesso!'
                tipo_msg = 'green'
                return render(request, 'blocos/mensagem_cadastro_concluido_servidor.html',
                              {'form': form, 'method': 'post', 'id': id, 'msg': msg, 'tipo_msg': tipo_msg,
                               'id_servidor': user.id})
            else:
                print(form.errors)
                msg = 'Erros encontrados!'
                tipo_msg = 'red'

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id, 'msg': msg, 'tipo_msg': tipo_msg, 'id_group_user' : id_group_user})


def ServidorDelete(request, id):
    servidor = ServidorModel.objects.get(pk=id)
    servidor.excluido = True
    servidor.save()
    return ListaServidores(request, msg="Servidor excluído com sucesso!", tipo_msg="green")


def ListaServidores(request, msg=None, tipo_msg=None):
    servidores = ServidorModel.objects.filter(excluido=False)
    dados, page_range, ultima = pagination(servidores, request.GET.get('page'))
    return render(request, 'servidores.html', {'dados': dados, 'page_range': page_range, 'ultima': ultima, 'msg': msg, 'tipo_msg': tipo_msg})
