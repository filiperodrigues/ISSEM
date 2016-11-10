# coding:utf-8
from django.shortcuts import render
from django.views.generic.base import View


class Pagina404View(View):
    template = '404.html'

    def get(self, request):
        return render(request, self.template)
