from django.contrib import admin
from issem.models.cid import Cid
from issem.models.departamento import Departamento
from issem.models.procedimento_medico import Procedimento_Medico
from issem.models.beneficio import Beneficio
from issem.models.funcao import Funcao
from issem.models.cargo import Cargo
from issem.models.tipo_dependente import Tipo_Dependente
from issem.models.tipo_exame import Tipo_Exame
from issem.models.secretaria import Secretaria
from issem.models.local_trabalho import Local_Trabalho

admin.site.register(Cid)
admin.site.register(Departamento)
admin.site.register(Procedimento_Medico)
admin.site.register(Beneficio)
admin.site.register(Funcao)
admin.site.register(Cargo)
admin.site.register(Tipo_Dependente)
admin.site.register(Tipo_Exame)
admin.site.register(Secretaria)
admin.site.register(Local_Trabalho)


## SOMENTE PARA TESTES ##
from issem.models.estado_civil import Estado_Civil
from issem.models.tipo_sangue import Tipo_Sangue
from issem.models.estado import Estado
from issem.models.cidade import Cidade
admin.site.register(Estado_Civil)
admin.site.register(Tipo_Sangue)
admin.site.register(Estado)
admin.site.register(Cidade)