from django.db.models import query
from django.shortcuts import render

# Create your views here.
from .models import MkBairros, MkConexoes
from .models import MkCidades
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    bairros = MkBairros.objects.all()
    cidades = MkCidades.objects.all()

    for bairro in bairros:
        print(bairro.bairro)

    context = {
        'cidades': cidades,
        'bairros': bairros,
        'values': request.GET
    }


    return render(request, 'conexoes/index.html', context)


def search(request):
    bairros = MkBairros.objects.all()
    cidades = MkCidades.objects.all()

    queryset_list = MkConexoes.objects.all()

    

    if 'cidade' in request.GET:
        codcidade = request.GET['cidade']
        if codcidade:
            queryset_list = queryset_list.filter(cidade__exact=codcidade)

    if 'bairro' in request.GET:
        codbairro = request.GET['bairro']
        if codbairro:
            queryset_list = queryset_list.filter(bairro__exact=codbairro)

    paginator = Paginator(queryset_list, 50)
    page = request.GET.get('page')
    paged_conexoes = paginator.get_page(page)

    context = {
        'cidades': cidades,
        'bairros': bairros,
        'values': request.GET,
        'conexoes': paged_conexoes
    }
    return render(request, 'conexoes/index.html', context)