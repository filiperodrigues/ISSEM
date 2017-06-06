# coding:utf-8
from django.conf.urls import url
from django.views.generic import TemplateView
from issem import views
from issem.views import *
from issem.views.cruds.procedimentos_medicos import BuscaProcedimentosMedicosView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout', 'django.contrib.auth.views.logout', {'next_page': '/issem/login/'}, name='logout'),

    # PAINÉIS
    url(r'^funcionario/$', PaginaFuncionarioView.as_view(), name='funcionario'),
    url(r'^medico/$', PaginaMedicoView.as_view(), name='medico'),
    url(r'^segurado$', PaginaSeguradoView.as_view(), name='segurado'),

    # CID
    url(r'^cad/cid/$', CidView.as_view(), name='cad_cid'),
    url(r'^edita/cid/(?P<id>\d+)/$', CidView.as_view(), name='edita_cid'),
    url(r'^deleta/cid/(?P<id>[0-9]+)/$', CidView.CidDelete, name='deleta_cid'),
    url(r'^lista/cids/$', CidView.ListaCids, name='lista_cids'),
    url(r'^campo/lista/?$', CidView.ListaCids, name='campo_pesquisa_cids'),

    # BENEFÍCIO
    url(r'^cad/beneficio/$', BeneficioView.as_view(), name='cad_beneficio'),
    url(r'^edita/beneficio/(?P<id>\d+)/$', BeneficioView.as_view(), name='edita_beneficio'),
    url(r'^deleta/beneficio/(?P<id>[0-9]+)/$', BeneficioView.BeneficioDelete, name='deleta_beneficio'),
    url(r'^lista/beneficios/$', BeneficioView.ListaBeneficios, name='lista_beneficios'),

    # PROCEDIMENTO MÉDICO
    url(r'^cad/procedimento_medico/$', ProcedimentoMedicoView.as_view(), name='cad_procedimento_medico'),
    url(r'^edita/procedimento_medico/(?P<id>\d+)/$', ProcedimentoMedicoView.as_view(),
        name='edita_procedimento_medico'),
    url(r'^deleta/procedimento_medico/(?P<id>[0-9]+)/$', ProcedimentoMedicoView.ProcedimentoMedicoDelete,
        name='deleta_procedimento_medico'),
    url(r'^lista/procedimentos_medicos/$', ProcedimentoMedicoView.ListaProcedimentosMedicos, name='lista_procedimentos_medicos'),

    # FUNÇÃO
    url(r'^cad/funcao/$', FuncaoView.as_view(), name='cad_funcao'),
    url(r'^edita/funcao/(?P<id>\d+)/$', FuncaoView.as_view(), name='edita_funcao'),
    url(r'^deleta/funcao/(?P<id>[0-9]+)/$', FuncaoView.FuncaoDelete, name='deleta_funcao'),

    # CARGO
    url(r'^cad/cargo/$', CargoView.as_view(), name='cad_cargo'),
    url(r'^edita/cargo/(?P<id>\d+)/$', CargoView.as_view(), name='edita_cargo'),
    url(r'^deleta/cargo/(?P<id>[0-9]+)/$', CargoView.CargoDelete, name='deleta_cargo'),
    url(r'^atualiza/cargo/$', CargoView.AtualizaCargo, name='atualiza_cargo'),

    # TIPO DEPENDENTE
    url(r'^cad/tipo_dependente/$', TipoDependenteView.as_view(), name='cad_tipo_dependente'),
    url(r'^edita/tipo_dependente/(?P<id>\d+)/$', TipoDependenteView.as_view(), name='edita_tipo_dependente'),
    url(r'^deleta/tipo_dependente/(?P<id>[0-9]+)/$', TipoDependenteView.TipoDependenteDelete, name='deleta_tipo_dependente'),

    # TIPO EXAME
    url(r'^cad/tipo_exame/$', TipoExameView.as_view(), name='cad_tipo_exame'),
    url(r'^edita/tipo_exame/(?P<id>\d+)/$', TipoExameView.as_view(), name='edita_tipo_exame'),
    url(r'^deleta/tipo_exame/(?P<id>[0-9]+)/$', TipoExameView.TipoExameDelete, name='deleta_tipo_exame'),

    # SECRETARIA
    url(r'^cad/secretaria/$', SecretariaView.as_view(), name='cad_secretaria'),
    url(r'^edita/secretaria/(?P<id>\d+)/$', SecretariaView.as_view(), name='edita_secretaria'),
    url(r'^deleta/secretaria/(?P<id>[0-9]+)/$', SecretariaView.SecretariaDelete, name='deleta_secretaria'),
    url(r'^atualiza/secretaria/$', SecretariaView.AtualizaSecretaria, name='atualiza_secretaria'),

    # LOCAL DE TRABALHO
    url(r'^cad/local_trabalho/$', LocalTrabalhoView.as_view(), name='cad_local_trabalho'),
    url(r'^edita/local_trabalho/(?P<id>\d+)/$', LocalTrabalhoView.as_view(), name='edita_local_trabalho'),
    url(r'^deleta/local_trabalho/(?P<id>[0-9]+)/$', LocalTrabalhoView.LocalTrabalhoDelete, name='deleta_local_trabalho'),
    url(r'^atualiza/local_trabalho/$', LocalTrabalhoView.AtualizaLocalTrabalho, name='atualiza_local_trabalho'),

    # DEPENDENTE
    url(r'^cad/dependente/$', DependenteView.as_view(), name='cad_dependente'),
    url(r'^cad/dependente_segurado/(?P<id_segurado>\d+)/$', DependenteView.as_view(), name='cad_dependente_segurado'),
    url(r'^edita/dependente/(?P<id>\d+)/$', DependenteView.as_view(), name='edita_dependente'),
    url(r'^deleta/dependente/(?P<id>[0-9]+)/$', DependenteView.DependenteDelete, name='deleta_dependente'),
    url(r'^lista/dependentes/$', DependenteView.ListaDependentes, name='lista_dependentes'),
    url(r'^transferencia/$', TransferenciaSegurado.as_view(), name='transferencia'),
    url(r'^busca_segurado/(?P<id>\d+)/$', TransferenciaSegurado.as_view(), name='seleciona_segurado'),

    # SEGURADO
    url(r'^cad/segurado/$', SeguradoView.as_view(), name='cad_segurado'),
    url(r'^edita/segurado/(?P<id>\d+)/$', SeguradoView.as_view(), name='edita_segurado'),
    url(r'^deleta/segurado/(?P<id>[0-9]+)/$', SeguradoView.SeguradoDelete, name='deleta_segurado'),
    url(r'^lista/segurados/$', SeguradoView.ListaSegurados, name='lista_segurados'),
    url(r'^lista/requerimentos/segurado/(?P<id>[0-9]+)/$', views.ListaRequerimentosSegurado,
        name='requerimentos_segurado'),

    # SERVIDOR
    url(r'^cad/servidor/$', ServidorView.as_view(), name='cad_servidor'),
    url(r'^edita/servidor/(?P<id>\d+)/$', ServidorView.as_view(), name='edita_servidor'),
    url(r'^deleta/servidor/(?P<id>[0-9]+)/$', ServidorView.ServidorDelete, name='deleta_servidor'),
    url(r'^lista/servidores/$', ServidorView.ListaServidores, name='lista_servidores'),

    # SEGURADO / SERVIDOR
    url(r'^edita/senha/(?P<id>\d+)/(?P<id_group>\d+)/$', EditaSenhaView.as_view(), name='edita_senha'),

    # CIDADE / ESTADO
    url(r'^escolha_cidade_atual/$', CidadeView.as_view(), name='escolha_cidade_atual'),
    url(r'^escolha_cidade_local_trabalho/$', CidadeView.as_view(), name='escolha_cidade_local_trabalho'),

    # CONSULTA PARÂMETROS
    url(r'^edita/parametros_consulta/$', ParametrosConfiguracaoView.as_view(),
        name='edita_parametros_consulta'),

    # REQUERIMENTO / AGENDAMENTO
    url(r'^cad/requerimento/(?P<id_beneficio>\d+)/$', RequerimentoView.as_view(), name='cad_requerimento'),
    url(r'^cad/requerimento_servidor/(?P<id_beneficio>\d+)/$', RequerimentoServidorView.as_view(),
        name='cad_requerimento_servidor'),
    url(r'^edita/requerimento/servidor/(?P<id_requerimento>\d+)/(?P<id_agendamento>\d+)/$',
        RequerimentoServidorView.as_view(), name='edita_requerimento'),
    url(r'^deleta/requerimento/(?P<id_requerimento>[0-9]+)/(?P<id_agendamento>[0-9]+)/$',
        views.RequerimentoAgendamentoDelete, name='deleta_requerimento'),
    url(r'^deleta/requerimento_sem_agendamento/(?P<id>[0-9]+)/$',
        views.RequerimentoSemAgendamentoDelete, name='deleta_requerimento_sem_agendamento'),
    url(r'^gera/agendamento/(?P<id_requerimento>\d+)/$', GeraAgendamentoServidorView.as_view(),
        name='define_agendamento'),
    url(r'^agenda/$', views.ApresentaAgendamentos, name='tabela_agendamentos'),
    url(r'^agenda/requerimentos/sem/agendamento$', views.ApresentaRequerimentosSemAgendamento, name='tabela_agendamentos_sem_requerimento'),
    url(r'^agenda/medica/$', views.ApresentaAgendamentosMedico, name='agenda_medica'),
    url(r'^agenda/medica/filtro/$', views.ApresentaAgendamentosMedico, name='filtro_agenda'),
    url(r'^requerimentos_sem_agendamento/$', views.ApresentaRequerimentosSemAgendamento,
        name='tabela_requerimentos_sem_agendamento'),
    url(r'^comprovante_agendamento/pdf/(?P<id_agendamento>\d+)/(?P<id_usuario>\d+)/$',
        views.GeraComprovanteAgendamento, name='comprovante_agendamento'),

    # LAUDO
    url(r'^laudo/(?P<id>\d+)/$', LaudoView.VisualizarLaudo, name='visualizar_laudo'),
    url(r'^cad/laudo/$', LaudoView.as_view(), name='cad_laudo'),
    url(r'^lista/laudos/$', LaudoView.ListaLaudos, name='lista_laudos'),
    url(r'^laudo/adendo/(?P<id>\d+)/$', LaudoView.AdicionarAdendo, name='adicionar_adendo'),
    url(r'^busca_procedimentos_medicos/$', BuscaProcedimentosMedicosView.as_view(), name='busca_procedimentos_medicos'),

    # CONTATO ISSEM
    url(r'^cad/contato_issem/$', ContatoIssemView.as_view(), name='cad_contato_issem'),
    url(r'^edita/contato_issem/(?P<id>\d+)/$', ContatoIssemView.as_view(), name='edita_contato_issem'),
    url(r'^deleta/contato_issem/(?P<id>[0-9]+)/$', ContatoIssemView.ContatoIssemDelete, name='deleta_contato_issem'),
    url(r'^lista/contatos/$', ContatoIssemView.ListaContatosIssem, name='lista_contatos_issem'),

    # PERFIL
    url(r'^perfil/(?P<id>\d+)$', PerfilView.as_view(), name='perfil'),


    # 404
    url(r'', TemplateView.as_view(template_name='404.html'), name='404'),
]
