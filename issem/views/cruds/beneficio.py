# coding:utf-8
from django.http import Http404
from django.shortcuts import render
from issem.models import BeneficioModel
from issem.forms import BeneficioForm
from django.views.generic.base import View
from issem.views.pagination import pagination
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


class BeneficioView(View):
    template = 'cruds/beneficio.html'
    template_lista = 'listas/beneficios.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}
        if id:  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            try:
                beneficio = BeneficioModel.objects.get(pk=id, excluido=False)
            except BeneficioModel.DoesNotExist:
                raise Http404("Benefício não encontrado.")
            form = BeneficioForm(instance=beneficio)
        else:  # MODO CADASTRO: recebe o formulário vazio
            form = BeneficioForm()

        context_dict['form'] = form
        context_dict['id'] = id
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template, context_dict)

    @method_decorator(user_passes_test(group_test))
    def post(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        valido = False
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            try:
                beneficio = BeneficioModel.objects.get(pk=id, excluido=False)
            except:
                raise Http404("Benefício não encontrado.")
            form = BeneficioForm(instance=beneficio, data=request.POST)
            if form.is_valid():
                form.save()
                msg = 'Alterações realizadas com sucesso!'
                tipo_msg = 'green'
                valido = True
        else:  # CADASTRO NOVO
            id = None
            form = BeneficioForm(data=request.POST)
            if form.is_valid():
                form.save()
                msg = 'Benefício cadastrado com sucesso!'
                tipo_msg = 'green'
                form = BeneficioForm()
                valido = True

        if not valido:
            print(form.errors)
            msg = 'Erros encontrados!'
            tipo_msg = 'red'

        context_dict['form'] = form
        context_dict['id'] = id
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template, context_dict)

    @classmethod
    @method_decorator(user_passes_test(group_test))
    def ListaBeneficios(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        if request.GET:
            ''' SE EXISTIR PAGINAÇÃO OU FILTRO; CASO EXISTA FILTRO MAS NÃO EXISTA PAGINAÇÃO,
            FARÁ A PAGINAÇÃO COM VALOR IGUAL À ZERO '''
            if 'filtro' in request.GET:
                beneficio1 = BeneficioModel.objects.filter(descricao__icontains=request.GET.get('filtro'), excluido=False)
                beneficio2 = BeneficioModel.objects.filter(numero_portaria__icontains=request.GET.get('filtro'), excluido=False)
                beneficio3 = BeneficioModel.objects.filter(concessao__icontains=request.GET.get('filtro'), excluido=False)
                beneficios = list(beneficio1) + list(beneficio2) + list(beneficio3)
                beneficios = list(set(beneficios))
            else:
                beneficios = BeneficioModel.objects.filter(excluido=False)
        else:
            beneficios = BeneficioModel.objects.filter(excluido=False)

        dados, page_range, ultima = pagination(beneficios, request.GET.get('page'))
        context_dict['dados'] = dados
        context_dict['page_range'] = page_range
        context_dict['ultima'] = ultima
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        context_dict['filtro'] = request.GET.get('filtro')
        return render(request, self.template_lista, context_dict)

    @classmethod
    @method_decorator(user_passes_test(group_test))
    def BeneficioDelete(self, request, id=None):
        try:
            beneficio = BeneficioModel.objects.get(pk=id)
        except:
            raise Http404("Benefício não encontrado.")
        beneficio.excluido = True
        beneficio.save()
        msg = 'Benefício excluído com sucesso!'
        tipo_msg = 'green'
        return self.ListaBeneficios(request, msg, tipo_msg)
