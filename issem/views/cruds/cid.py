# coding:utf-8
from django.shortcuts import render
from issem.models import CidModel
from issem.forms import CidForm
from django.views.generic.base import View
from issem.views.pagination import pagination
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


class CidView(View):
    template = 'cruds/cid.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id=None, msg=None, tipo_msg=None):
        if id:  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            try:
                cid = CidModel.objects.get(pk=id)
                form = CidForm(instance=cid)
            except:
                msg = 'Não foi possível fazer a consulta!'
                tipo_msg = 'red'
                return CidView.ListaCids(request, msg, tipo_msg)
        else:  # MODO CADASTRO: recebe o formulário vazio
            form = CidForm()
        return render(request, self.template, {'form': form, 'id': id, 'msg': msg, 'tipo_msg': tipo_msg})

    @method_decorator(user_passes_test(group_test))
    def post(self, request, msg=None, tipo_msg=None):
        valido = False
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            try:
                cid = CidModel.objects.get(pk=id)
                form = CidForm(instance=cid, data=request.POST)
            except:
                msg = 'Ocorreram erros durante as alterações, tente novamente!'
                tipo_msg = 'red'
                return CidView.ListaCids(request, msg, tipo_msg)
            if form.is_valid():
                try:
                    form.save()
                except:
                    msg = 'Ocorreram erros durante as alterações, tente novamente!'
                    tipo_msg = 'red'
                    return CidView.ListaCids(request, msg, tipo_msg)
                msg = 'Alterações realizadas com sucesso!'
                tipo_msg = 'green'
                valido = True
        else:  # CADASTRO NOVO
            id = None
            form = CidForm(data=request.POST)
            if form.is_valid():
                try:
                    form.save()
                except:
                    msg = 'Ocorreram erros durante o cadastro, tente novamente!'
                    tipo_msg = 'red'
                    return CidView.ListaCids(request, msg, tipo_msg)
                msg = 'Benefício cadastrado com sucesso!'
                tipo_msg = 'green'
                form = CidForm()
                valido = True

        if not valido:
            print(form.errors)
            msg = 'Erros encontrados!'
            tipo_msg = 'red'

        return render(request, self.template, {'form': form, 'id': id, 'msg': msg, 'tipo_msg': tipo_msg})

    @classmethod
    @method_decorator(user_passes_test(group_test))
    def ListaCids(self, request, msg=None, tipo_msg=None):
        cids = CidModel.objects.filter(excluido=0)
        dados, page_range, ultima = pagination(cids, request.GET.get('page'))
        return render(request, 'listas/cids.html',
                      {'dados': dados, 'page_range': page_range, 'ultima': ultima, 'msg': msg, 'tipo_msg': tipo_msg})

    @classmethod
    @method_decorator(user_passes_test(group_test))
    def CidDelete(self, request, id):
        try:
            cid = CidModel.objects.get(pk=id)
            cid.excluido = True
            cid.save()
            msg = 'Exclusão efetuada com sucesso!'
            tipo_msg = 'green'
        except:
            msg = 'Ocorreu erro durante a exclusão!'
            tipo_msg = 'red'
        return CidView.ListaCids(request, msg, tipo_msg)