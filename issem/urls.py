# coding:utf-8
from django.conf.urls import url
from django.views.generic import TemplateView

from issem import views
from issem.views import *


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/issem/login/'}, name='logout'),


    ## PÁGINAS ##
    url(r'^funcionario/$', PaginaFuncionarioView.as_view(), name='funcionario'),
    url(r'^medico/$', PaginaMedicoView.as_view(), name='medico'),
    url(r'^segurado$', PaginaSeguradoView.as_view(), name='segurado'),

    ## DEPARTAMENTO ##
    url(r'^cad/departamento/$', DepartamentoView.as_view(), name='cad_departamento'),
    url(r'^edita/departamento/(?P<id>\d+)/$', DepartamentoView.as_view(), name='edita_departamento'),
    url(r'^deleta/departamento/(?P<id>[0-9]+)/$', views.DepartamentoDelete, name='deleta_departamento'),

    ## CID ##
    url(r'^cad/cid/$', CidView.as_view(), name='cad_cid'),
    url(r'^edita/cid/(?P<id>\d+)/$', CidView.as_view(), name='edita_cid'),
    url(r'^deleta/cid/(?P<id>[0-9]+)/$', views.CidDelete, name='deleta_cid'),

    ## BENEFÍCIO ##
    url(r'^cad/beneficio/$', BeneficioView.as_view(), name='cad_beneficio'),
    url(r'^edita/beneficio/(?P<id>\d+)/$', BeneficioView.as_view(), name='edita_beneficio'),
    url(r'^deleta/beneficio/(?P<id>[0-9]+)/$', views.BeneficioDelete, name='deleta_beneficio'),

    ## PROCEDIMENTO MÉDICO ##
    url(r'^cad/procedimento_medico/$', ProcedimentoMedicoView.as_view(), name='cad_procedimento_medico'),
    url(r'^edita/procedimento_medico/(?P<id>\d+)/$', ProcedimentoMedicoView.as_view(), name='edita_procedimento_medico'),
    url(r'^deleta/procedimento_medico/(?P<id>[0-9]+)/$', views.ProcedimentoMedicoDelete, name='deleta_procedimento_medico'),

    ## FUNÇÃO ##
    url(r'^cad/funcao/$', FuncaoView.as_view(), name='cad_funcao'),
    url(r'^edita/funcao/(?P<id>\d+)/$', FuncaoView.as_view(), name='edita_funcao'),
    url(r'^deleta/funcao/(?P<id>[0-9]+)/$', views.FuncaoDelete, name='deleta_funcao'),

    ## CARGO ##
    url(r'^cad/cargo/$', CargoView.as_view(), name='cad_cargo'),
    url(r'^edita/cargo/(?P<id>\d+)/$', CargoView.as_view(), name='edita_cargo'),
    url(r'^deleta/cargo/(?P<id>[0-9]+)/$', views.CargoDelete, name='deleta_cargo'),

    ## TIPO DEPENDENTE ##
    url(r'^cad/tipo_dependente/$', TipoDependenteView.as_view(), name='cad_tipo_dependente'),
    url(r'^edita/tipo_dependente/(?P<id>\d+)/$', TipoDependenteView.as_view(), name='edita_tipo_dependente'),
    url(r'^deleta/tipo_dependente/(?P<id>[0-9]+)/$', views.TipoDependenteDelete, name='deleta_tipo_dependente'),

    ## TIPO EXAME ##
    url(r'^cad/tipo_exame/$', TipoExameView.as_view(), name='cad_tipo_exame'),
    url(r'^edita/tipo_exame/(?P<id>\d+)/$', TipoExameView.as_view(), name='edita_tipo_exame'),
    url(r'^deleta/tipo_exame/(?P<id>[0-9]+)/$', views.TipoExameDelete, name='deleta_tipo_exame'),

    ## SECRETARIA ##
    url(r'^cad/secretaria/$', SecretariaView.as_view(), name='cad_secretaria'),
    url(r'^edita/secretaria/(?P<id>\d+)/$', SecretariaView.as_view(), name='edita_secretaria'),
    url(r'^deleta/secretaria/(?P<id>[0-9]+)/$', views.SecretariaDelete, name='deleta_secretaria'),

    ## LOCAL DE TRABALHO ##
    url(r'^cad/local_trabalho/$', LocalTrabalhoView.as_view(), name='cad_local_trabalho'),
    url(r'^edita/local_trabalho/(?P<id>\d+)/$', LocalTrabalhoView.as_view(), name='edita_local_trabalho'),
    url(r'^deleta/local_trabalho/(?P<id>[0-9]+)/$', views.LocalTrabalhoDelete, name='deleta_local_trabalho'),

    ## DEPENDENTE ##
    url(r'^cad/dependente/$', DependenteView.as_view(), name='cad_dependente'),
    url(r'^edita/dependente/(?P<id>\d+)/$', DependenteView.as_view(), name='edita_dependente'),
    url(r'^deleta/dependente/(?P<id>[0-9]+)/$', views.DependenteDelete, name='deleta_dependente'),

    ## SEGURADO ##
    url(r'^cad/segurado/$', SeguradoView.as_view(), name='cad_segurado'),
    url(r'^edita/segurado/(?P<id>\d+)/$', SeguradoView.as_view(), name='edita_segurado'),
    url(r'^deleta/segurado/(?P<id>[0-9]+)/$', views.SeguradoDelete, name='deleta_segurado'),
    url(r'^apresenta/segurado/$', views.ApresentaSegurado, name='apresenta_segurado'),

    ## SERVIDOR ##
    url(r'^cad/servidor/$', ServidorView.as_view(), name='cad_servidor'),
    url(r'^edita/servidor/(?P<id>\d+)/$', ServidorView.as_view(), name='edita_servidor'),
    url(r'^deleta/servidor/(?P<id>[0-9]+)/$', views.ServidorDelete, name='deleta_servidor'),
    url(r'^apresenta/servidor/$', views.ApresentaServidor, name='apresenta_servidor'),

    ## CIDADE / ESTADO ##
    url(r'^escolha_cidade_natural/$', CidadeView.as_view(), name='escolha_cidade_natural'),
    url(r'^escolha_cidade_atual/$', CidadeView.as_view(), name='escolha_cidade_atual'),
    url(r'^escolha_cidade_local_trabalho/$', CidadeView.as_view(), name='escolha_cidade_local_trabalho'),

    ## CONSULTA PARÂMETROS ##
    url(r'^cad/consulta_parametro/$', ConstultaParametrosView.as_view(), name='cad_consulta_parametros'),
    url(r'^edita/consulta_parametro/(?P<id>\d+)/$', ConstultaParametrosView.as_view(), name='edita_consulta_parametros'),
    url(r'^deleta/consulta_parametro/(?P<id>[0-9]+)/$', views.ConsultaParametrosDelete, name='deleta_consulta_parametros'),

    ## REQUERIMENTO / AGENDAMENTO ##
    url(r'^cad/requerimento/(?P<id_beneficio>\d+)/$', RequerimentoView.as_view(), name='cad_requerimento'),
    url(r'^cad/requerimento_servidor/(?P<id_beneficio>\d+)/$', RequerimentoServidorView.as_view(), name='cad_requerimento_servidor'),
    url(r'^edita/requerimento/servidor/(?P<id_requerimento>\d+)/(?P<id_agendamento>\d+)/$', RequerimentoServidorView.as_view(), name='edita_requerimento'),
    url(r'^deleta/requerimento/(?P<id_requerimento>[0-9]+)/(?P<id_agendamento>[0-9]+)/$', views.RequerimentoAgendamentoDelete, name='deleta_requerimento'),
    url(r'^gera/agendamento/(?P<id_requerimento>\d+)/$', GeraAgendamentoServidorView.as_view(),name='define_agendamento'),
    url(r'^agenda/$', views.ApresentaAgendamentos, name='tabela_agendamentos'),
    url(r'^requerimentos_sem_agendamento/$', views.ApresentaRequerimentosSemAgendamento, name='tabela_requerimentos_sem_agendamento'),

    ## 404 ##
    url(r'', TemplateView.as_view(template_name='404.html'), name='404'),
]
