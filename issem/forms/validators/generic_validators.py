# coding: utf-8
from django import forms
from datetime import datetime
from dateutil.relativedelta import relativedelta


def ValidarDataInicialFinal(data_inicial, data_final):

    if not data_inicial:
        raise forms.ValidationError("Defina uma data inicial")
    elif not data_final:
        raise forms.ValidationError("Defina uma data final")

    if data_inicial <= data_final:
        return data_final
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