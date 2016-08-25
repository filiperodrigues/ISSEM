# coding:utf-8
from django.conf.urls import url
from issem import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    ## DEPARTAMENTO ##
    url(r'^add_departamento/$', views.add_departamento, name='add_departamento'),
    url(r'^edita_departamento/(?P<id>[0-9]+)/$', views.edita_departamento, name='edita_departamento'),
    url(r'^deleta_departamento/(?P<id>[0-9]+)/$', views.deleta_departamento, name='deleta_departamento'),

    ## CID ##
    url(r'^add_cid/$', views.add_cid, name='add_cid'),
    url(r'^edita_cid/(?P<id>[0-9]+)/$', views.edita_cid, name='edita_cid'),
    url(r'^deleta_cid/(?P<id>[0-9]+)/$', views.deleta_cid, name='deleta_cid'),

    ## BENEFÍCIO ##
    url(r'^add_beneficio/$', views.add_beneficio, name='add_beneficio'),
    url(r'^edita_beneficio/(?P<id>[0-9]+)/$', views.edita_beneficio, name='edita_beneficio'),
    url(r'^deleta_beneficio/(?P<id>[0-9]+)/$', views.deleta_beneficio, name='deleta_beneficio'),

    ## PROCEDIMENTO MÉDICO ##
    url(r'^add_procedimento_medico/$', views.add_procedimento_medico, name='add_procedimento_medico'),
    url(r'^edita_procedimento_medico/(?P<id>[0-9]+)/$', views.edita_procedimento_medico,
        name='edita_procedimento_medico'),
    url(r'^deleta_procedimento_medico/(?P<id>[0-9]+)/$', views.deleta_procedimento_medico,
        name='deleta_procedimento_medico'),

    ## FUNÇÃO ##
    url(r'^add_funcao/$', views.add_funcao, name='add_funcao'),
    url(r'^edita_funcao/(?P<id>[0-9]+)/$', views.edita_funcao, name='edita_funcao'),
    url(r'^deleta_funcao/(?P<id>[0-9]+)/$', views.deleta_funcao, name='deleta_funcao'),

    ## CARGO ##
    url(r'^add_cargo/$', views.add_cargo, name='add_cargo'),
    url(r'^edita_cargo/(?P<id>[0-9]+)/$', views.edita_cargo, name='edita_cargo'),
    url(r'^deleta_cargo/(?P<id>[0-9]+)/$', views.deleta_cargo, name='deleta_cargo'),

    ## TIPO DEPENDENTE ##
    url(r'^add_tipo_dependente/$', views.add_tipo_dependente, name='add_tipo_dependente'),
    url(r'^edita_tipo_dependente/(?P<id>[0-9]+)/$', views.edita_tipo_dependente, name='edita_tipo_dependente'),
    url(r'^deleta_tipo_dependente/(?P<id>[0-9]+)/$', views.deleta_tipo_dependente, name='deleta_tipo_dependente'),

    ## TIPO EXAME ##
    url(r'^add_tipo_exame/$', views.add_tipo_exame, name='add_tipo_exame'),
    url(r'^edita_tipo_exame/(?P<id>[0-9]+)/$', views.edita_tipo_exame, name='edita_tipo_exame'),
    url(r'^deleta_tipo_exame/(?P<id>[0-9]+)/$', views.deleta_tipo_exame, name='deleta_tipo_exame'),

    ## TIPO SANGUE ##
    url(r'^add_tipo_sangue/$', views.add_tipo_sangue, name='add_tipo_sangue'),
    url(r'^edita_tipo_sangue/(?P<id>[0-9]+)/$', views.edita_tipo_sangue, name='edita_tipo_sangue'),
    url(r'^deleta_tipo_sangue/(?P<id>[0-9]+)/$', views.deleta_tipo_sangue, name='deleta_tipo_sangue'),

    ## ESTADO CIVIL ##
    url(r'^add_estado_civil/$', views.add_estado_civil, name='add_estado_civil'),
    url(r'^edita_estado_civil/(?P<id>[0-9]+)/$', views.edita_estado_civil, name='edita_estado_civil'),
    url(r'^deleta_estado_civil/(?P<id>[0-9]+)/$', views.deleta_estado_civil, name='deleta_estado_civil'),
    
    ## SECRETARIA ##
    url(r'^add_secretaria/$', views.add_secretaria, name='add_secretaria'),
    url(r'^edita_secretaria/(?P<id>[0-9]+)/$', views.edita_secretaria, name='edita_secretaria'),
    url(r'^deleta_secretaria/(?P<id>[0-9]+)/$', views.deleta_secretaria, name='deleta_secretaria'),
    
    ## LOCAL DE TRABALHO ##
    url(r'^add_local_trabalho/$', views.add_local_trabalho, name='add_local_trabalho'),
    url(r'^edita_local_trabalho/(?P<id>[0-9]+)/$', views.edita_local_trabalho, name='edita_local_trabalho'),
    url(r'^deleta_local_trabalho/(?P<id>[0-9]+)/$', views.deleta_local_trabalho, name='deleta_local_trabalho'),

    ## DEPENDENTE ##
    url(r'^add_dependente/$', views.add_dependente, name='add_dependente'),
    url(r'^edita_dependente/(?P<id>[0-9]+)/$', views.edita_dependente, name='edita_dependente'),
    url(r'^deleta_dependente/(?P<id>[0-9]+)/$', views.deleta_dependente, name='deleta_dependente'),

    ## SEGURADO ##
    url(r'^add_segurado/$', views.add_segurado, name='add_segurado'),
    url(r'^edita_segurado/(?P<id>[0-9]+)/$', views.edita_segurado, name='edita_segurado'),
    url(r'^deleta_segurado/(?P<id>[0-9]+)/$', views.deleta_segurado, name='deleta_segurado'),

    ## SERVIDOR ##
    url(r'^add_servidor/$', views.add_servidor, name='add_servidor'),
    url(r'^edita_servidor/(?P<id>[0-9]+)/$', views.edita_servidor, name='edita_servidor'),
    url(r'^deleta_servidor/(?P<id>[0-9]+)/$', views.deleta_servidor, name='deleta_servidor'),
]
