#coding:utf-8
from django.conf.urls import include, url
from django.contrib import admin
from issem import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^issem/', include('issem.urls', namespace="issem")),
    url(r'^$', views.index, name='index'),
]
