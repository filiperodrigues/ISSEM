from django.contrib import admin
from issem.models import Departamento, Cid, Procedimento_Medico, Beneficio, Funcao, Cargo, Tipo_Dependente

admin.site.register(Departamento)
admin.site.register(Cid)
admin.site.register(Procedimento_Medico)
admin.site.register(Beneficio)
admin.site.register(Funcao)
admin.site.register(Cargo)
admin.site.register(Tipo_Dependente)