# coding:utf-8
from django.contrib.auth.models import Group
from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse

from issem.models.servidor import ServidorModel


def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('issem:login'))

    grupos = request.user.groups.all()
    request.session['administrador'] = False

    if not request.user.is_superuser:
        if len(grupos) > 0:
            if len(grupos) > 1:
                if 'grupo_sessao' not in request.session:
                    return HttpResponseRedirect(reverse('issem:escolha_papel'))
                else:
                    grupo = request.session['grupo_sessao']
            else:
                grupo = str(grupos[0])
                request.session['grupo_sessao'] = grupo

            if grupo == "Tecnico":
                return HttpResponseRedirect(reverse('issem:medico'))
            elif grupo == 'Segurado':
                return HttpResponseRedirect(reverse('issem:segurado'))
            elif grupo == 'Administrativo':
                request.session['administrador'] = ServidorModel.objects.get(pk=request.user.id).administrador
                return HttpResponseRedirect(reverse('issem:funcionario'))
            else:
                return render(request, 'paineis/index.html')
        else:
            return render(request, 'paineis/index.html', {'msg': 'Ocorreu algum erro no login, verifique e tente novamente.',
                                                          'tipo_msg': 'red'})
    else:
        return render(request, 'paineis/index.html')


def escolha_papel(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('issem:login'))

    context_dict = {}

    if 'gp' in request.GET:
        id = int(request.GET.get('gp'))
        grupo_escolhido = Group.objects.get(pk=id)
        if grupo_escolhido in request.user.groups.all():
            request.session['grupo_sessao'] = grupo_escolhido.name
            return HttpResponseRedirect(reverse('issem:index'))
        else:
            context_dict['msg'] = 'Permissão negada!'
            context_dict['tipo_msg'] = 'red'

    context_dict['grupos'] = request.user.groups.all()
    return render(request, 'paineis/escolha_papel.html', context_dict)
