# coding:utf-8
from django.shortcuts import render
from issem.models import ConsultaParametrosModel
from issem.forms import ConsultaParametrosForm
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


class ParametrosConsultaView(View):
    template = 'cruds/parametros_consulta.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        try:
            consulta_parametros = ConsultaParametrosModel.objects.get(pk=1)
            form = ConsultaParametrosForm(instance=consulta_parametros)
        except:
            msg = 'Não foi possível fazer a consulta!'
            tipo_msg = 'red'
            context_dict['msg'] = msg
            context_dict['tipo_msg'] = tipo_msg
            return render(request, 'paineis/funcionario_pagina.html', context_dict)
        context_dict['form'] = form
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        context_dict['id'] = 1
        return render(request, self.template, context_dict)

    @method_decorator(user_passes_test(group_test))
    def post(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        valido = False
        try:
            consulta_parametros = ConsultaParametrosModel.objects.get(pk=1)
            form = ConsultaParametrosForm(instance=consulta_parametros, data=request.POST)
        except:
            msg = 'Ocorreram erros duranthe as alterações, tente novamente!'
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

        if not valido:
            print(form.errors)
            msg = 'Erros encontrados!'
            tipo_msg = 'red'

        return render(request, self.template, {'form': form, 'id': id, 'msg': msg, 'tipo_msg': tipo_msg})
