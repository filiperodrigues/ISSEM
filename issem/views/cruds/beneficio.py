# coding:utf-8
from django.shortcuts import render
from issem.models import BeneficioModel
from issem.forms import BeneficioForm
from django.views.generic.base import View
from issem.views.pagination import pagination
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


class BeneficioView(View):
    template = 'cruds/beneficio.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id=None, msg=None, tipo_msg=None):
        if id:  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            try:
                beneficio = BeneficioModel.objects.get(pk=id, excluido=0)
                form = BeneficioForm(instance=beneficio)
            except:
                msg = 'Não foi possível fazer a consulta!'
                tipo_msg = 'red'
                return BeneficioView.ListaBeneficios(request, msg, tipo_msg)
        else:  # MODO CADASTRO: recebe o formulário vazio
            form = BeneficioForm()
        return render(request, self.template, {'form': form, 'id': id, 'msg': msg, 'tipo_msg': tipo_msg})

    @method_decorator(user_passes_test(group_test))
    def post(self, request, msg=None, tipo_msg=None):
        valido = False
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            try:
                beneficio = BeneficioModel.objects.get(pk=id, excluido=0)
                form = BeneficioForm(instance=beneficio, data=request.POST)
            except:
                msg = 'Ocorreram erros durante as alterações, tente novamente!'
                tipo_msg = 'red'
                return BeneficioView.ListaBeneficios(request, msg, tipo_msg)
            if form.is_valid():
                try:
                    form.save()
                except:
                    msg = 'Ocorreram erros durante as alterações, tente novamente!'
                    tipo_msg = 'red'
                    return BeneficioView.ListaBeneficios(request, msg, tipo_msg)
                msg = 'Alterações realizadas com sucesso!'
                tipo_msg = 'green'
                valido = True
        else:  # CADASTRO NOVO
            id = None
            form = BeneficioForm(data=request.POST)
            if form.is_valid():
                try:
                    form.save()
                except:
                    msg = 'Ocorreram erros durante o cadastro, tente novamente!'
                    tipo_msg = 'red'
                    return BeneficioView.ListaBeneficios(request, msg, tipo_msg)
                msg = 'Benefício cadastrado com sucesso!'
                tipo_msg = 'green'
                form = BeneficioForm()
                valido = True

        if not valido:
            print(form.errors)
            msg = 'Erros encontrados!'
            tipo_msg = 'red'

        return render(request, self.template, {'form': form, 'id': id, 'msg': msg, 'tipo_msg': tipo_msg})

    @classmethod
    @method_decorator(user_passes_test(group_test))
    def ListaBeneficios(self, request, msg=None, tipo_msg=None):
        if request.GET:
            beneficio1 = BeneficioModel.objects.filter(descricao__contains=request.GET.get('campo'), excluido=0)
            beneficio2 = BeneficioModel.objects.filter(concessao__contains=request.GET.get('campo'), excluido=0)
            beneficio3 = BeneficioModel.objects.filter(numero_portaria__contains=request.GET.get('campo'), excluido=0)
            beneficios = list(beneficio1) + list(beneficio2) + list(beneficio3)
            beneficios = list(set(beneficios))

        else:
            beneficios = BeneficioModel.objects.filter(excluido=0)
        dados, page_range, ultima = pagination(beneficios, request.GET.get('page'))
        return render(request, 'listas/beneficios.html',
                      {'dados': dados, 'page_range': page_range, 'ultima': ultima, 'msg': msg, 'tipo_msg': tipo_msg})

    @classmethod
    @method_decorator(user_passes_test(group_test))
    def BeneficioDelete(self, request, id=None):
        try:
            beneficio = BeneficioModel.objects.get(pk=id)
            beneficio.excluido = True
            beneficio.save()
            msg = 'Exclusão efetuada com sucesso!'
            tipo_msg = 'green'
        except:
            msg = 'Ocorreu erro durante a exclusão!'
            tipo_msg = 'red'
        return BeneficioView.ListaBeneficios(request, msg, tipo_msg)
