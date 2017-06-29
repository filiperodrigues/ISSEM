# coding:utf-8
from django.http import Http404
from django.shortcuts import render
from issem.models import ServidorModel, SeguradoModel, DependenteModel
from django.views.generic.base import View
from django.contrib.auth.models import User
from datetime import date
from dateutil.relativedelta import relativedelta


class PerfilView(View):
    template = 'estatico/perfil.html'

    def get(self, request, id=None):
        context_dict = {}

        try:
            usuario = User.objects.get(pk=id)
        except:
            raise Http404("Usuário não encontrado.")
        try:
            grupo = usuario.groups.get()
        except:
            raise Http404("Grupo do usuário não encontrado.")

        if str(grupo) == "Administrativo" or str(grupo) == "Tecnico":
            administrador = ServidorModel.objects.get(pk=request.user.id)
            context_dict['administrador'] = administrador
            grupo = False
            try:
                usuario = ServidorModel.objects.get(pk=id)
            except:
                raise Http404("Usuário não encontrado.")
        elif str(grupo) == 'Segurado':
            grupo = False
            try:
                usuario = SeguradoModel.objects.get(pk=id)
            except:
                raise Http404("Segurado não encontrado.")
            dependentes = usuario.dependente.filter(excluido=False)
            context_dict['dependentes'] = VerificaValidadeDependente(dependentes)
        elif str(grupo) == 'Dependente':
            grupo = False
            try:
                usuario = DependenteModel.objects.get(pk=id)
            except:
                raise Http404("Usuário não encontrado.")
            try:
                segurado = SeguradoModel.objects.get(dependente__id=id)
            except:
                segurado = None
            context_dict['segurado'] = segurado
        else:
            raise Http404("Grupo do usuário não encontrado.")

        usuario_logado = User.objects.get(pk=request.user.id)
        context_dict['id'] = id
        context_dict['group_user'] = grupo
        context_dict['usuario'] = usuario
        context_dict['usuario_logado'] = usuario_logado.id
        return render(request, self.template, context_dict)


def VerificaValidadeDependente(dependentes):
    hoje_menos_dezoito_ano = date.today() - relativedelta(years=18)
    lista_retorno = []
    for dependente in dependentes:
        if dependente.data_nascimento >= hoje_menos_dezoito_ano or dependente.tipo == "Incapaz":
            lista_retorno.append(dependente)
        else:
            dependente.excluido = True
            dependente.save()
    return lista_retorno

