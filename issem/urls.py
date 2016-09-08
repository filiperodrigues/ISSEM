# coding:utf-8
from django.conf.urls import url
from issem import views
from issem.views import *


urlpatterns = [
    url(r'^$', views.index, name='index'),
    ## PÁGINAS ##
    url(r'^funcionario$', views.PaginaFuncionarioView, name='funcionario'),
    url(r'^medico$', views.PaginaMedicoView, name='medico'),


    ## DEPARTAMENTO ##
    url(r'^add/departamento/$', DepartamentoView.as_view(), name='add_departamento'),
    url(r'^edita/departamento/(?P<id>\d+)/$', DepartamentoView.as_view(), name='edita_departamento'),
    url(r'^deleta/departamento/(?P<id>[0-9]+)/$', views.DepartamentoDelete, name='deleta_departamento'),

    ## CID ##
    url(r'^add/cid/$', CidView.as_view(), name='add_cid'),
    url(r'^edita/cid/(?P<id>\d+)/$', CidView.as_view(), name='edita_cid'),
    url(r'^deleta/cid/(?P<id>[0-9]+)/$', views.CidDelete, name='deleta_cid'),

    ## BENEFÍCIO ##
    url(r'^add/beneficio/$', BeneficioView.as_view(), name='add_beneficio'),
    url(r'^edita/beneficio/(?P<id>\d+)/$', BeneficioView.as_view(), name='edita_beneficio'),
    url(r'^deleta/beneficio/(?P<id>[0-9]+)/$', views.BeneficioDelete, name='deleta_beneficio'),

    ## PROCEDIMENTO MÉDICO ##
    url(r'^add/procedimento_medico/$', ProcedimentoMedicoView.as_view(), name='add_procedimento_medico'),
    url(r'^edita/procedimento_medico/(?P<id>\d+)/$', ProcedimentoMedicoView.as_view(), name='edita_procedimento_medico'),
    url(r'^deleta/procedimento_medico/(?P<id>[0-9]+)/$', views.ProcedimentoMedicoDelete, name='deleta_procedimento_medico'),

    ## FUNÇÃO ##
    url(r'^add/funcao/$', FuncaoView.as_view(), name='add_funcao'),
    url(r'^edita/funcao/(?P<id>\d+)/$', FuncaoView.as_view(), name='edita_funcao'),
    url(r'^deleta/funcao/(?P<id>[0-9]+)/$', views.FuncaoDelete, name='deleta_funcao'),

    ## CARGO ##
    url(r'^add/cargo/$', CargoView.as_view(), name='add_cargo'),
    url(r'^edita/cargo/(?P<id>\d+)/$', CargoView.as_view(), name='edita_cargo'),
    url(r'^deleta/cargo/(?P<id>[0-9]+)/$', views.CargoDelete, name='deleta_cargo'),

    ## TIPO DEPENDENTE ##
    url(r'^add/tipo_dependente/$', TipoDependenteView.as_view(), name='add_tipo_dependente'),
    url(r'^edita/tipo_dependente/(?P<id>\d+)/$', TipoDependenteView.as_view(), name='edita_tipo_dependente'),
    url(r'^deleta/tipo_dependente/(?P<id>[0-9]+)/$', views.TipoDependenteDelete, name='deleta_tipo_dependente'),

    ## TIPO EXAME ##
    url(r'^add/tipo_exame/$', TipoExameView.as_view(), name='add_tipo_exame'),
    url(r'^edita/tipo_exame/(?P<id>\d+)/$', TipoExameView.as_view(), name='edita_tipo_exame'),
    url(r'^deleta/tipo_exame/(?P<id>[0-9]+)/$', views.TipoExameDelete, name='deleta_tipo_exame'),

    ## TIPO SANGUE ##
    url(r'^add/tipo_sanguineo/$', TipoSanguineoView.as_view(), name='add_tipo_sanguineo'),
    url(r'^edita/tipo_sanguineo/(?P<id>\d+)/$', TipoSanguineoView.as_view(), name='edita_tipo_sanguineo'),
    url(r'^deleta/tipo_sanguineo/(?P<id>[0-9]+)/$', views.TipoSanguineoDelete, name='deleta_tipo_sanguineo'),

    ## ESTADO CIVIL ##
    url(r'^add/estado_civil/$', EstadoCivilView.as_view(), name='add_estado_civil'),
    url(r'^edita/estado_civil/(?P<id>\d+)/$', EstadoCivilView.as_view(), name='edita_estado_civil'),
    url(r'^deleta/estado_civil/(?P<id>[0-9]+)/$', views.EstadoCivilDelete, name='deleta_estado_civil'),
    
    ## SECRETARIA ##
    url(r'^add/secretaria/$', SecretariaView.as_view(), name='add_secretaria'),
    url(r'^edita/secretaria/(?P<id>\d+)/$', SecretariaView.as_view(), name='edita_secretaria'),
    url(r'^deleta/secretaria/(?P<id>[0-9]+)/$', views.SecretariaDelete, name='deleta_secretaria'),
    
    ## LOCAL DE TRABALHO ##
    url(r'^add/local_trabalho/$', LocalTrabalhoView.as_view(), name='add_local_trabalho'),
    url(r'^edita/local_trabalho/(?P<id>\d+)/$', LocalTrabalhoView.as_view(), name='edita_local_trabalho'),
    url(r'^deleta/local_trabalho/(?P<id>[0-9]+)/$', views.LocalTrabalhoDelete, name='deleta_local_trabalho'),

    ## DEPENDENTE ##
    url(r'^add/dependente/$', DependenteView.as_view(), name='add_dependente'),
    url(r'^edita/dependente/(?P<id>\d+)/$', DependenteView.as_view(), name='edita_dependente'),
    url(r'^deleta/dependente/(?P<id>[0-9]+)/$', views.DependenteDelete, name='deleta_dependente'),

    ## SEGURADO ##
    url(r'^add/segurado/$', SeguradoView.as_view(), name='add_segurado'),
    url(r'^edita/segurado/(?P<id>\d+)/$', SeguradoView.as_view(), name='edita_segurado'),
    url(r'^deleta/segurado/(?P<id>[0-9]+)/$', views.SeguradoDelete, name='deleta_segurado'),
    url(r'^apresenta/segurado/$', views.ApresentaSegurado, name='apresenta_segurado'),

    ## SERVIDOR ##
    url(r'^add/servidor/$', ServidorView.as_view(), name='add_servidor'),
    url(r'^edita/servidor/(?P<id>\d+)/$', ServidorView.as_view(), name='edita_servidor'),
    url(r'^deleta/servidor/(?P<id>[0-9]+)/$', views.ServidorDelete, name='deleta_servidor'),
    url(r'^apresenta/servidor/$', views.ApresentaServidor, name='apresenta_servidor'),
]
