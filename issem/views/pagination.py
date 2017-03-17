from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def pagination(model, page):
    paginator = Paginator(model, 3)
    try:
        dados = paginator.page(page)
    except PageNotAnInteger:
        dados = paginator.page(1)
    except EmptyPage:
        dados = paginator.page(paginator.num_pages)
    return(dados)