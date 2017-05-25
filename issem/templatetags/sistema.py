from django import template

from issem.models import ParametrosConfiguracaoModel

# TODO criar um metodo no manager para 'Sistema.objects.order_by('data')' esta duplicando codigo
register = template.Library()


@register.simple_tag
def issem_info():
    dados = ParametrosConfiguracaoModel.objects.all().last()
    if dados:
        return dados.descricao_issem
    return None

@register.simple_tag
def informacoes_rodape():
    dados = ParametrosConfiguracaoModel.objects.all().last()
    if dados:
        return dados.informacoes_rodape
    return None