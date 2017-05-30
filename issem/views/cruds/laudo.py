# coding:utf-8
from django.http import Http404
from django.shortcuts import render, HttpResponseRedirect
from issem.models import LaudoModel, ServidorModel, SeguradoModel
from issem.forms import LaudoForm
from django.views.generic.base import View
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator


# TODO


class LaudoView(View):
    template = 'cruds/laudo.html'
    template_lista = 'listas/laudos.html'
    template_laudo = 'estatico/visualizar_laudo.html'
    template_adendo = 'cruds/adendo.html'

    def group_test(user):
        return user.groups.filter(name='Tecnico')

    @method_decorator(user_passes_test(group_test))
    def get(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}
        if id:
            try:
                laudo = LaudoModel.objects.get(pk=id, excluido=False)  # MODO EDIÇÃO: pega as informações do objeto através do ID (PK)
            except:
                raise Http404("Laudo médico não encontrado.")
            form = LaudoForm(instance=laudo)
        else:
            form = LaudoForm()  # MODO CADASTRO: recebe o formulário vazio

        context_dict['medico'] = ServidorModel.objects.get(pk=request.user.id)
        context_dict['form'] = form
        context_dict['id'] = id
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        return render(request, self.template, context_dict)

    @method_decorator(user_passes_test(group_test))
    def post(self, request, id_laudo=None):
        if request.POST['id']:  # EDIÇÃO
            id = request.POST['id']
            laudo = LaudoModel.objects.get(pk=id, excluido=False)
            form = LaudoForm(instance=laudo, data=request.POST)
        else:  # CADASTRO NOVO
            id = None
            form = LaudoForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print(form.errors)

        return render(request, self.template, {'form': form, 'method': 'post', 'id': id})

    @classmethod
    def LaudoDelete(self, request, id):
        laudo = LaudoModel.objects.get(pk=id)
        laudo.excluido = True
        laudo.save()
        return HttpResponseRedirect('/')

    @classmethod
    def ListaLaudos(self, request, msg=None, tipo_msg=None):
        context_dict = {}

        from issem.views import pagination, CidModel
        laudos = CidModel.objects.all()

        dados, page_range, ultima = pagination(laudos, request.GET.get('page'))
        context_dict['dados'] = dados
        context_dict['page_range'] = page_range
        context_dict['ultima'] = ultima
        context_dict['msg'] = msg
        context_dict['tipo_msg'] = tipo_msg
        context_dict['filtro'] = request.GET.get('filtro')
        return render(request, self.template_lista, context_dict)

    @classmethod
    def VisualizarLaudo(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}
        return render(request, self.template_laudo, context_dict)

    @classmethod
    def AdicionarAdendo(self, request, id=None, msg=None, tipo_msg=None):
        context_dict = {}
        return render(request, self.template_adendo, context_dict)