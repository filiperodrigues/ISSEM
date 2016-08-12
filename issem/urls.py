from django.conf.urls import patterns, url
from issem import views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', views.index, name='index'),

	url(r'^add_departamento/$', views.add_departamento, name='add_departamento'),
	url(r'^add_cid/$', views.add_cid, name='add_cid'),
	url(r'^delete_cid/(?P<id>[0-9]+)/$', views.delete_cid, name='delete_cid'),
	url(r'^edita_cid/(?P<id>[0-9]+)/$', views.edita_cid, name='edita_cid'),

]
