# coding:utf-8
from django.http import Http404
from django.shortcuts import render
from issem.models.contato_issem import ContatoIssemModel
from issem.forms.contato_issem import ContatoIssemForm
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


class ContatoIssemView(View):
    template = 'cruds/contato_issem.html'
    template_lista = 'listas/contatos_issem.html'

    def group_test(user):
        return user.groups.filter(name='Administrativo')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}
        if id:  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            try:
                contato_issem = ContatoIssemModel.objects.get(pk=id)
            except:
                raise Http404("Contato não encontrado.")
            form = ContatoIssemForm(instance=contato_issem)
        else:  # MODO CADASTRO: recebe o formulário vazio
            form = ContatoIssemForm()

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
                contato_issem = ContatoIssemModel.objects.get(pk=id)
            except:
                raise Http404("Contato não encontrado.")
            form = ContatoIssemForm(instance=contato_issem, data=request.POST)
            if form.is_valid():
                form.save()
                msg = 'Alterações realizadas com sucesso!'
                tipo_msg = 'green'
                valido = True
        else:  # CADASTRO NOVO
            id = None
            form = ContatoIssemForm(data=request.POST)
            if form.is_valid():
                form.save()
                msg = 'Contato cadastrado com sucesso!'
                tipo_msg = 'green'
                form = ContatoIssemForm()
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
    def ListaContatosIssem(self, request, msg=None, tipo_msg=None):
        context_dict = {}
        context_dict['dados'] = ContatoIssemModel.objects.all()
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template_lista, context_dict)

    @classmethod
    @method_decorator(user_passes_test(group_test))
    def ContatoIssemDelete(self, request, id=None):
        try:
            contato_issem = ContatoIssemModel.objects.get(pk=id)
        except:
            raise Http404("Contato não encontrado.")
        contato_issem.delete()
        msg = 'Exclusão efetuada com sucesso!'
        tipo_msg = 'green'
        return self.ListaContatosIssem(request, msg, tipo_msg)
