from django.contrib import admin
from issem.models import Departamento, Cid, Procedimento_Medico, Beneficios

# Register your models here.
admin.site.register(Departamento)
admin.site.register(Cid)
admin.site.register(Procedimento_Medico)
admin.site.register(Beneficios)