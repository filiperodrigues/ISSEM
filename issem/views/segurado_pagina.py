from issem.models import BeneficioModel
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator


class PaginaSeguradoView(View):
    template = 'segurado_pagina.html'

    def group_test(user):
        return user.groups.filter(name='Segurado')

    @method_decorator(user_passes_test(group_test))

    def get(self, request):
        context_dict = {}
        context_dict['beneficios'] = BeneficioModel.objects.all()
        context_dict['msg'] = 0
        return render(request, 'segurado_pagina.html', context_dict)
