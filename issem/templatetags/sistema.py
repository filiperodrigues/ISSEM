from django import template

from issem.models import ParametrosConfiguracaoModel

# TODO criar um metodo no manager para 'Sistema.objects.order_by('data')' esta duplicando codigo
register = template.Library()


@register.simple_tag
def issem_info():
    try:
        dados = ParametrosConfiguracaoModel.objects.all().last().descricao_issem
    except:
        dados = ""
    return dados


@register.simple_tag
def informacoes_rodape():
    try:
        dados = ParametrosConfiguracaoModel.objects.all().last().informacoes_rodape
    except:
        dados = ""
    return dados