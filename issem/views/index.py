# coding:utf-8
from django.shortcuts import render
from issem.models import *


def index(request):
    context_dict = {}
    context_dict['departamentos'] = DepartamentoModel.objects.all()
    context_dict['cids'] = CidModel.objects.all()
    context_dict['procedimentos_medicos'] = ProcedimentoMedicoModel.objects.all()
    context_dict['beneficios'] = BeneficioModel.objects.all()
    context_dict['funcoes'] = FuncaoModel.objects.all()
    context_dict['cargos'] = CargoModel.objects.all()
    context_dict['tipo_dependente'] = TipoDependenteModel.objects.all()
    context_dict['tipo_exame'] = TipoExameModel.objects.all()
    context_dict['tipo_sangue'] = TipoSangueModel.objects.all()
    context_dict['estado_civil'] = EstadoCivilModel.objects.all()
    context_dict['secretaria'] = SecretariaModel.objects.all()
    context_dict['local_trabalho'] = LocalTrabalhoModel.objects.all()
    context_dict['dependentes'] = DependenteModel.objects.all()
    context_dict['segurados'] = SeguradoModel.objects.all()
    context_dict['servidores'] = ServidorModel.objects.all()

    return render(request, 'index.html', context_dict)