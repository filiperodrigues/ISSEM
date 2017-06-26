# coding:utf-8
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from issem import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^issem/', include('issem.urls', namespace="issem")),
    url(r'^tinymce/', include('tinymce.urls')),

    # ALTERAÇÃO DE SENHA
    url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'password_reset/password_reset_form.html',
                                                          'email_template_name': 'password_reset/password_reset_email.html',
                                                          'subject_template_name': 'password_reset/password_reset_subject.txt'},
        name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done,
        {'template_name': 'password_reset/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, {'template_name': 'password_reset/password_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete,
        {'template_name': 'password_reset/password_reset_complete.html'}, name='password_reset_complete'),

]
