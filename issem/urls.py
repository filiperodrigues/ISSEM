from django.conf.urls import patterns, url
from issem import views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', views.index, name='index'),

	url(r'^add_departamento/$', views.add_departamento, name='add_departamento'),
	url(r'^add_cid/$', views.add_cid, name='add_cid'),

]
