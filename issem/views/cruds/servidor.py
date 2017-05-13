# coding:utf-8
from django.http import Http404
from django.shortcuts import render
from issem.models import ServidorModel
from issem.forms import ServidorFormCad, ServidorFormEdit
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group
from issem.views.pagination import pagination


class ServidorView(View):
    template = 'cruds/servidor.html'
    template_lista = 'listas/servidores.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo') or user.groups.filter(name='Tecnico')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}
        if id:  # EDIÇÃO
            try:
                servidor = ServidorModel.objects.get(pk=id, excluido=0)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            except:
                raise Http404("Servidor não encontrado.")
            form = ServidorFormEdit(instance=servidor)
            try:
                group_user = Group.objects.get(user=id)
            except:
                raise Http404("Grupo do usuário não encontrado.")
            id_group_user = group_user.id
        else:  # CADASTRO NOVO
            form = ServidorFormCad()  # MODO CADASTRO: recebe o formulário vazio
            id_group_user = ""

        context_dict['form'] = form
        context_dict['id'] = id
        context_dict['id_group_user'] = id_group_user
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template, context_dict)

    # TODO: REFATORAR
    @method_decorator(user_passes_test(group_test))
    def post(self, request, id=None, msg=None, tipo_msg=None):
        id_group_user = None

        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            try:
                servidor = ServidorModel.objects.get(pk=id, excluido=0)
            except:
                raise Http404("Servidor não encontrado.")
            form = ServidorFormEdit(instance=servidor, data=request.POST)
            try:
                group_user = Group.objects.get(user=id)
            except:
                raise Http404("Grupo do usuário não encontrado.")
            id_group_user = group_user.id

            if form.is_valid():
                form.save(commit=False)
                group_user.user_set.remove(id)
                servidor.groups.add(form.cleaned_data['groups'])
                servidor.save()

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
                if id != None:
                    if Group.objects.get(user=id):
                        group_name = Group.objects.get(user=id)
                        group_name.user_set.remove(id)

                gp = Group.objects.get(id=request.POST["groups"])
                user = ServidorModel.objects.get(username=request.POST["username"])
                user.groups.add(gp)
                user.save()
                msg = 'Cadastro efetuado com sucesso!'
                tipo_msg = 'green'
                form = ServidorFormCad()
                return render(request, self.template, {'form': form, 'msg': msg, 'tipo_msg': tipo_msg})
            else:
                print(form.errors)
                msg = 'Erros encontrados!'
                tipo_msg = 'red'

        return render(request, self.template,
                      {'form': form, 'method': 'post', 'id': id, 'msg': msg, 'tipo_msg': tipo_msg,
                       'id_group_user': id_group_user})

    @classmethod
    def ServidorDelete(self, request, id):
        try:
            servidor = ServidorModel.objects.get(pk=id)
        except:
            raise Http404("Servidor não encontrado.")
        servidor.excluido = True
        servidor.save()
        msg = "Servidor excluído com sucesso!"
        tipo_msg = "green"
        return self.ListaServidores(request, msg, tipo_msg)

    @classmethod
    def ListaServidores(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        if request.GET or 'page' in request.GET:
            if request.GET.get('filtro'):
                servidor1 = ServidorModel.objects.filter(cpf__icontains=request.GET.get('filtro'), excluido=0)
                servidor2 = ServidorModel.objects.filter(nome__icontains=request.GET.get('filtro'), excluido=0)
                servidor3 = ServidorModel.objects.filter(email__icontains=request.GET.get('filtro'), excluido=0)
                servidores = list(servidor1) + list(servidor2) + list(servidor3)
                servidores = list(set(servidores))
            else:
                servidores = ServidorModel.objects.filter(excluido=False)
        else:
            servidores = ServidorModel.objects.filter(excluido=False)

        dados, page_range, ultima = pagination(servidores, request.GET.get('page'))
        context_dict['dados'] = dados
        context_dict['page_range'] = page_range
        context_dict['ultima'] = ultima
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        context_dict['filtro'] = request.GET.get('filtro')
        return render(request, self.template_lista, context_dict)
