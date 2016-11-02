# coding:utf-8
from django.shortcuts import render
from issem.models import *

from django.contrib.auth.decorators import login_required, user_passes_test



from django.shortcuts import HttpResponse, HttpResponseRedirect
#@login_required(login_url='/login.html')
#@group_required('Servidor')


def index(request):



    context_dict = {}
    context_dict['departamentos'] = DepartamentoModel.objects.all()
    context_dict['cids'] = CidModel.objects.all()
    context_dict['procedimentos_medicos'] = ProcedimentoMedicoModel.objects.all()
    context_dict['beneficios'] = BeneficioModel.objects.all()
    context_dict['funcoes'] = FuncaoModel.objects.all()
    context_dict['cargos'] = CargoModel.objects.all()
    context_dict['tipos_dependente'] = TipoDependenteModel.objects.all()
    context_dict['tipos_exame'] = TipoExameModel.objects.all()
    context_dict['secretarias'] = SecretariaModel.objects.all()
    context_dict['locais_trabalho'] = LocalTrabalhoModel.objects.all()
    context_dict['dependentes'] = DependenteModel.objects.all()
    context_dict['segurados'] = SeguradoModel.objects.all()
    context_dict['servidores'] = ServidorModel.objects.all()
    context_dict['consulta_parametros'] = ConsultaParametrosModel.objects.all()
    context_dict['agendamentos'] = AgendamentoModel.objects.all()
    context_dict['requerimentos'] = RequerimentoModel.objects.all()

    return render(request, 'index.html', context_dict)