#coding:utf-8
from django.conf.urls import patterns, url
from issem import views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', views.index, name='index'),
	#Departamento
	url(r'^add_departamento/$', views.add_departamento, name='add_departamento'),
	url(r'^edita_departamento/(?P<id>[0-9]+)/$', views.edita_departamento, name='edita_departamento'),
	url(r'^delete_departamento/(?P<id>[0-9]+)/$', views.delete_departamento, name='delete_departamento'),
	#CID
	url(r'^add_cid/$', views.add_cid, name='add_cid'),
	url(r'^edita_cid/(?P<id>[0-9]+)/$', views.edita_cid, name='edita_cid'),
	url(r'^delete_cid/(?P<id>[0-9]+)/$', views.delete_cid, name='delete_cid'),
	#Beneficios
	url(r'^add_beneficios/$', views.add_beneficios, name='add_beneficios'),
	url(r'^edit_beneficios/(?P<id>[0-9]+)/$', views.edit_beneficios, name='edit_beneficios'),
	url(r'^delete_beneficios/(?P<id>[0-9]+)/$', views.delete_beneficios, name= 'delete_beneficios'),
	#Procedimentos
	url(r'^add_procedimento_medico/$', views.add_procedimento_medico, name='add_procedimento_medico'),
	url(r'^edit_procedimento_medico/(?P<id>[0-9]+)/$', views.edit_procedimento_medico, name='edit_procedimento_medico'),
	url(r'^delete_procedimento_medico/(?P<id>[0-9]+)/$', views.delete_procedimento_medico, name= 'delete_procedimento_medico'),
	#FUNÇÃO#
	url(r'^add_funcao/$', views.add_funcao, name='add_funcao'),
	url(r'^edita_funcao/(?P<id>[0-9]+)/$', views.edita_funcao, name='edita_funcao'),
	url(r'^delete_funcao/(?P<id>[0-9]+)/$', views.delete_funcao, name='delete_funcao'),
	#CARGO#
	url(r'^add_cargo/$', views.add_cargo, name='add_cargo'),
	url(r'^edita_cargo/(?P<id>[0-9]+)/$', views.edita_cargo, name='edita_cargo'),
	url(r'^delete_cargo/(?P<id>[0-9]+)/$', views.delete_cargo, name='delete_cargo'),

]
