# coding: utf-8
from django.contrib import admin

from issem.models.agendamento import AgendamentoModel
from issem.models.beneficio import BeneficioModel
from issem.models.cargo import CargoModel
from issem.models.cid import CidModel
from issem.models.consulta_parametros import ConsultaParametrosModel
from issem.models.dependente import DependenteModel
from issem.models.exame_requerimento import ExameRequerimentoModel
from issem.models.funcao import FuncaoModel
from issem.models.lixeira.departamento import DepartamentoModel
from issem.models.local_trabalho import LocalTrabalhoModel
from issem.models.procedimento_medico import ProcedimentoMedicoModel
from issem.models.requerimento import RequerimentoModel
from issem.models.secretaria import SecretariaModel
from issem.models.segurado import SeguradoModel
from issem.models.servidor import ServidorModel
from issem.models.tipo_dependente import TipoDependenteModel
from issem.models.tipo_exame import TipoExameModel
from issem.models.contato_issem import ContatoIssemModel

admin.site.register(CidModel)
admin.site.register(DepartamentoModel)
admin.site.register(ProcedimentoMedicoModel)
admin.site.register(BeneficioModel)
admin.site.register(FuncaoModel)
admin.site.register(CargoModel)
admin.site.register(TipoDependenteModel)
admin.site.register(TipoExameModel)
admin.site.register(SecretariaModel)
admin.site.register(LocalTrabalhoModel)
admin.site.register(ServidorModel)
admin.site.register(DependenteModel)
admin.site.register(SeguradoModel)
admin.site.register(ConsultaParametrosModel)
admin.site.register(RequerimentoModel)
admin.site.register(ExameRequerimentoModel)
admin.site.register(AgendamentoModel)
admin.site.register(ContatoIssemModel)




## SOMENTE PARA TESTES, POIS ESTES NÃO SERÃO PREENCHIDOS PELOS USUÁRIOS ##
from issem.models.estado_civil import EstadoCivilModel
from issem.models.tipo_sanguineo import TipoSanguineoModel
from issem.models.estado import EstadoModel
from issem.models.cidade import CidadeModel
admin.site.register(EstadoCivilModel)
admin.site.register(TipoSanguineoModel)
admin.site.register(EstadoModel)
admin.site.register(CidadeModel)