# coding:utf-8
from django.http import Http404
from django.shortcuts import render
from issem.models import CidModel
from issem.forms import CidForm
from django.views.generic.base import View
from issem.views.pagination import pagination
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


class CidView(View):
    template = 'cruds/cid.html'
    template_lista = 'listas/cids.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id=None, msg=None, tipo_msg=None, var_controle = None):
        context_dict = {}
        if id:  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            try:
                cid = CidModel.objects.get(pk=id, excluido=False)
            except:
                raise Http404("CID não encontrado.")
            form = CidForm(instance=cid)
        else:  # MODO CADASTRO: recebe o formulário vazio
            form = CidForm()

        context_dict['form'] = form
        context_dict['id'] = id
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template, context_dict)

    @method_decorator(user_passes_test(group_test))
    def post(self, request, msg=None, tipo_msg=None, var_controle = None):
        context_dict = {}
        valido = False
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            try:
                cid = CidModel.objects.get(pk=id, excluido=False)
            except:
                raise Http404("CID não encontrado.")
            form = CidForm(instance=cid, data=request.POST)
            if form.is_valid():
                form.save()
                msg = 'Alterações realizadas com sucesso!'
                tipo_msg = 'green'
                valido = True
        else:  # CADASTRO NOVO
            id = None
            form = CidForm(data=request.POST)
            if form.is_valid():
                form.save()
                msg = 'CID cadastrado com sucesso!'
                tipo_msg = 'green'
                form = CidForm()
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
    def ListaCids(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        if request.GET:
            ''' SE EXISTIR PAGINAÇÃO OU FILTRO; CASO EXISTA FILTRO MAS NÃO EXISTA PAGINAÇÃO,
            FARÁ A PAGINAÇÃO COM VALOR IGUAL À ZERO '''
            if 'filtro' in request.GET:
                cid1 = CidModel.objects.filter(descricao__icontains=request.GET.get('filtro'), excluido=False)
                cid2 = CidModel.objects.filter(cod_cid__icontains=request.GET.get('filtro'), excluido=False)
                cid3 = CidModel.objects.filter(gravidade__icontains=request.GET.get('filtro'), excluido=False)
                cids = list(cid1) + list(cid2) + list(cid3)
                cids = list(set(cids))
            else:
                cids = CidModel.objects.filter(excluido=False)
        else:
            cids = CidModel.objects.filter(excluido=False)

        dados, page_range, ultima = pagination(cids, request.GET.get('page'))
        context_dict['dados'] = dados
        context_dict['page_range'] = page_range
        context_dict['ultima'] = ultima
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        context_dict['filtro'] = request.GET.get('filtro')
        return render(request, self.template_lista, context_dict)

    @classmethod
    @method_decorator(user_passes_test(group_test))
    def CidDelete(self, request, id=None):
        try:
            cid = CidModel.objects.get(pk=id)
        except:
            raise Http404("CID não encontrado.")
        cid.excluido = True
        cid.save()
        msg = 'Exclusão efetuada com sucesso!'
        tipo_msg = 'green'
        return self.ListaCids(request, msg, tipo_msg)
