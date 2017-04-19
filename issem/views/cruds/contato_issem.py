# coding:utf-8
from django.shortcuts import render
from issem.models import ContatoIssemModel
from issem.forms import ContatoIssemForm
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


class ContatoIssemView(View):
    template = 'cruds/contato_issem.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id=None, msg=None, tipo_msg=None):
        if id:  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            try:
                contato_issem = ContatoIssemModel.objects.get(pk=id)
                form = ContatoIssemForm(instance=contato_issem)
            except:
                msg = 'Não foi possível fazer a consulta!'
                tipo_msg = 'red'
                return ContatoIssemView.ListaContatosIssem(request, msg, tipo_msg)
        else:  # MODO CADASTRO: recebe o formulário vazio
            form = ContatoIssemForm()
        return render(request, self.template, {'form': form, 'id': id, 'msg': msg, 'tipo_msg': tipo_msg})

    @method_decorator(user_passes_test(group_test))
    def post(self, request, msg=None, tipo_msg=None):
        valido = False
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            try:
                contato_issem = ContatoIssemModel.objects.get(pk=id)
                form = ContatoIssemForm(instance=contato_issem, data=request.POST)
            except:
                msg = 'Ocorreram erros durante as alterações, tente novamente!'
                tipo_msg = 'red'
                return ContatoIssemView.ListaContatosIssem(request, msg, tipo_msg)
            if form.is_valid():
                try:
                    form.save()
                except:
                    msg = 'Ocorreram erros durante as alterações, tente novamente!'
                    tipo_msg = 'red'
                    return ContatoIssemView.ListaContatosIssem(request, msg, tipo_msg)
                msg = 'Alterações realizadas com sucesso!'
                tipo_msg = 'green'
                valido = True
        else:  # CADASTRO NOVO
            id = None
            form = ContatoIssemForm(data=request.POST)
            if form.is_valid():
                try:
                    form.save()
                except:
                    msg = 'Ocorreram erros durante o cadastro, tente novamente!'
                    tipo_msg = 'red'
                    return ContatoIssemView.ListaContatosIssem(request, msg, tipo_msg)
                msg = 'Benefício cadastrado com sucesso!'
                tipo_msg = 'green'
                form = ContatoIssemForm()
                valido = True

        if not valido:
            print(form.errors)
            msg = 'Erros encontrados!'
            tipo_msg = 'red'

        return render(request, self.template, {'form': form, 'id': id, 'msg': msg, 'tipo_msg': tipo_msg})

    @classmethod
    def ListaContatosIssem(self, request, msg=None, tipo_msg=None):
        dados = ContatoIssemModel.objects.all()
        return render(request, 'listas/contatos_issem.html',
                      {'dados': dados, 'msg': msg, 'tipo_msg': tipo_msg})

    @classmethod
    @method_decorator(user_passes_test(group_test))
    def ContatoIssemDelete(self, request, id=None):
        try:
            contato_issem = ContatoIssemModel.objects.get(pk=id)
            contato_issem.delete()
            msg = 'Exclusão efetuada com sucesso!'
            tipo_msg = 'green'
        except:
            msg = 'Ocorreu erro durante a exclusão!'
            tipo_msg = 'red'
        return ContatoIssemView.ListaContatosIssem(request, msg, tipo_msg)
