from django.conf.urls import patterns, url
from issem import views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', views.index, name='index'),
]
