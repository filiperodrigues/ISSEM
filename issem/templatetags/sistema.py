from django import template

from issem.models import ParametrosConfiguracaoModel

# TODO criar um metodo no manager para 'Sistema.objects.order_by('data')' esta duplicando codigo
register = template.Library()


@register.simple_tag
def issem_info():
    dados = ParametrosConfiguracaoModel.objects.all().last()
    if dados.descricao_issem:
        return dados.descricao_issem
    else:
        return ""


@register.simple_tag
def informacoes_rodape():
    dados = ParametrosConfiguracaoModel.objects.all().last()
    if dados.informacoes_rodape:
        return dados.informacoes_rodape
    return ""
