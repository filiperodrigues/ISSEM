from django.conf.urls import patterns, url
from issem import views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^add_procedimento_medico/$', views.add_procedimento_medico, name='add_procedimento_medico'),
	url(r'^add_departamento/$', views.add_departamento, name='add_departamento'),
	url(r'^add_cid/$', views.add_cid, name='add_cid'),
	url(r'^add_beneficios/$', views.add_beneficios, name='add_beneficios'),
	url(r'^delete_procedimento_medico/(?P<id>[0-9]+)/$', views.delete_procedimento_medico, name= 'delete_procedimento_medico'),
	url(r'^delete_beneficios/(?P<id>[0-9]+)/$', views.delete_beneficios, name= 'delete_beneficios'),
	url(r'^edit_beneficios/(?P<id>[0-9]+)/$', views.edit_beneficios, name='edit_beneficios'),
	url(r'^edit_procedimento_medico/(?P<id>[0-9]+)/$', views.edit_procedimento_medico, name='edit_procedimento_medico'),
]
