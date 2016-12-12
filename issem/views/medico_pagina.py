# coding:utf-8
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator


class PaginaMedicoView(View):
    template = 'medico_pagina.html'

    def group_test(user):
        return user.groups.filter(name='Técnico')

    @method_decorator(user_passes_test(group_test))

    def get(self, request):
        return render(request, self.template)