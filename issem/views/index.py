# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from issem.models import ParametrosConfiguracaoModel


def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('issem:login'))

    grupos = request.user.groups.all()

    if len(grupos) > 0:
        grupo_1 = str(grupos[0])

        if grupo_1 == "Tecnico":
            return HttpResponseRedirect(reverse('issem:medico'))
        elif grupo_1 == 'Segurado':
            return HttpResponseRedirect(reverse('issem:segurado'))
        elif grupo_1 == 'Administrativo':
            return HttpResponseRedirect(reverse('issem:funcionario'))
        else:
            return render(request, 'paineis/index.html')

    return render(request, 'paineis/index.html')
