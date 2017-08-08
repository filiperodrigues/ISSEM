# coding: utf-8
from django import forms
from datetime import datetime
from dateutil.relativedelta import relativedelta

from django.contrib.auth.models import User


def ValidaPrimeiroNome(first_name):
    if not first_name:
        raise forms.ValidationError("Este campo é obrigatório")
    else:
        return first_name


def ValidaSegundoNome(last_name):
    if not last_name:
        raise forms.ValidationError("Este campo é obrigatório")
    else:
        return last_name


def ValidaEmail(email, instance_id):
    if not email:
        raise forms.ValidationError("Este campo é obrigatório")
    elif User.objects.filter(email=email).exclude(pk=instance_id):
        raise forms.ValidationError("Este e-mail já existe")
    else:
        return email


def ValidaEmailDependente(email, instance_id):
    if email:
        if User.objects.filter(email=email).exclude(pk=instance_id):
            raise forms.ValidationError("Este e-mail já existe")
        else:
            return email
    else:
        return email


def ValidaCRM(crm, groups):
    if str(groups) == "Tecnico":
        if crm:
            return crm
        else:
            raise forms.ValidationError("Digite um CRM.")
    else:
        return crm


def ValidarDataInicialFinal(data_inicial, data_final):

    if not data_inicial:
        raise forms.ValidationError("Defina uma data inicial")
    elif not data_final:

        raise forms.ValidationError("Defina uma data final")

    if data_inicial <= data_final:
        return data_final
    else:
        raise forms.ValidationError("Data final deve ser após a data inicial")


def ValidarDataRequerimento(data_inicial, data_final):

    if not data_inicial:
        raise forms.ValidationError("Defina uma data inicial")
    elif not data_final:
        raise forms.ValidationError("Defina uma data final")

    if data_inicial <= data_final:
        qtd_dias = int(str((data_final - data_inicial)).split()[0])
        if qtd_dias > 15:
            return data_final
        else:
            raise forms.ValidationError("Deve ser maior que 15(quinze) dias.")
    else:
        raise forms.ValidationError("Data final deve ser após a data inicial")


def ValidarPassword(password, password_checker):
    if password != password_checker:
        raise forms.ValidationError("Senhas diferentes")
    else:
        return password_checker


def ValidarDataNascimento(data):
    data_gerada = datetime.now() - relativedelta(years=18)
    data_gerada = data_gerada.date()
    if data == None:
        raise forms.ValidationError("Este campo é obrigatório.")
    elif data <= data_gerada:
        return data
    else:
        raise forms.ValidationError("Deve ter mais que 18 anos")


def ValidarDataNascimentoDependente(data, tipo):
    data_gerada = datetime.now() - relativedelta(years=18)
    data_gerada = data_gerada.date()
    if data == None:
        raise forms.ValidationError("Este campo é obrigatório.")
    elif data >= data_gerada:
        return tipo
    else:
        raise forms.ValidationError("Dependentes não incapazes devem ter mais de 18 anos")


def ValidarTamanhoPassword(senha):
    if len(senha) >= 6:
        return senha
    else:
        raise forms.ValidationError("A senha deve conter no mínimo 6 caracteres")
