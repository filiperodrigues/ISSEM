# coding:utf-8
from django.shortcuts import render, get_object_or_404
from issem.models import CargoModel
from issem.forms import CargoForm
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


class CargoView(View):
    template = 'cruds/cargo.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}
        if id:  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            try:
                cargo = get_object_or_404(CargoModel, pk=id)
                form = CargoForm(instance=cargo)
            except:
                msg = 'Não foi possível fazer a consulta!'
                tipo_msg = 'red'
                context_dict['msg'] = msg
                context_dict['tipo_msg'] = tipo_msg
                return render(request, 'paineis/funcionario_pagina.html', context_dict)
        else:  # MODO CADASTRO: recebe o formulário vazio
            form = CargoForm()
        return render(request, self.template, {'form': form, 'id': id, 'msg': msg, 'tipo_msg': tipo_msg})

    @method_decorator(user_passes_test(group_test))
    def post(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        valido = False
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            try:
                cargo = CargoModel.objects.get(pk=id)
                form = CargoForm(instance=cargo, data=request.POST)
            except:
                msg = 'Ocorreram erros durante as alterações, tente novamente!'
                tipo_msg = 'red'
                context_dict['msg'] = msg
                context_dict['tipo_msg'] = tipo_msg
                return render(request, 'paineis/funcionario_pagina.html', context_dict)
            if form.is_valid():
                try:
                    form.save()
                except:
                    msg = 'Ocorreram erros durante as alterações, tente novamente!'
                    tipo_msg = 'red'
                    context_dict['msg'] = msg
                    context_dict['tipo_msg'] = tipo_msg
                    return render(request, 'paineis/funcionario_pagina.html', context_dict)
                msg = 'Alterações realizadas com sucesso!'
                tipo_msg = 'green'
                valido = True
        else:  # CADASTRO NOVO
            id = None
            form = CargoForm(data=request.POST)
            if form.is_valid():
                try:
                    form.save()
                except:
                    msg = 'Ocorreram erros durante o cadastro, tente novamente!'
                    tipo_msg = 'red'
                    context_dict['msg'] = msg
                    context_dict['tipo_msg'] = tipo_msg
                    return render(request, 'paineis/funcionario_pagina.html', context_dict)
                msg = 'Benefício cadastrado com sucesso!'
                tipo_msg = 'green'
                form = CargoForm()
                valido = True

        if not valido:
            print(form.errors)
            msg = 'Erros encontrados!'
            tipo_msg = 'red'

        return render(request, self.template, {'form': form, 'id': id, 'msg': msg, 'tipo_msg': tipo_msg})

    @classmethod
    @method_decorator(user_passes_test(group_test))
    def CargoDelete(self, request, id):
        context_dict = {}
        try:
            cargo = CargoModel.objects.get(pk=id)
            # cargo.excluido = True
            # cargo.save()
            msg = 'Exclusão efetuada com sucesso!'
            tipo_msg = 'green'
        except:
            msg = 'Ocorreu erro durante a exclusão!'
            tipo_msg = 'red'

        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, 'paineis/funcionario_pagina.html', context_dict)
