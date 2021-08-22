from django.db.models import query
from django.db.models.expressions import F, RawSQL
from django.shortcuts import render
from datetime import datetime
from django.db.models import Count

# Create your views here.
from .models import MkBairros, MkConexoes, MkContratos, MkRadacct
from .models import MkCidades
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    bairros = MkBairros.objects.all()
    cidades = MkCidades.objects.all()

    # for bairro in bairros:
    #     print(bairro.bairro)

    context = {
        'cidades': cidades,
        'bairros': bairros,
        'values': request.GET
    }


    return render(request, 'conexoes/index.html', context)


def search(request):
    bairros = MkBairros.objects.all()
    cidades = MkCidades.objects.all()

    queryset_list = MkRadacct.objects.all()

    choices = {}

    if 'cidade' in request.GET:
        codcidade = request.GET['cidade']
        
        if codcidade:
            choices['cidade'] = MkCidades.objects.get(pk=codcidade)
            queryset_list = queryset_list.select_related('mkconn_user').filter(mkconn_user__cidade__exact=codcidade)

    if 'bairro' in request.GET:
        codbairro = request.GET['bairro']       

        if codbairro:
            choices['bairro'] = MkBairros.objects.get(pk=codbairro)
            queryset_list = queryset_list.select_related('mkconn_user').filter(mkconn_user__bairro__exact=codbairro)
    
    if 'username' in request.GET:
        username = request.GET['username']
        if username:
            queryset_list = queryset_list.filter(mkconn_user__username__icontains=username)

    if 'data_inicial' in request.GET:
        data_inicial = request.GET['data_inicial']
        
        if data_inicial:
            if 'data_final' in request.GET:
                data_final = request.GET['data_final']
                if data_final:
                    queryset_list = queryset_list.filter(acctstartdate__range=[data_inicial, data_final])
                    
                else:
                    queryset_list = queryset_list.filter(acctstartdate__range=[data_inicial, data_final])
        elif 'data_final' in request.GET:
                data_final = request.GET['data_final']
                if data_final:
                    queryset_list = queryset_list.filter(acctstartdate__lte=data_final)
    
    print('QUERY: ', queryset_list.query)

    queryset_list = queryset_list.annotate(Count('mkconn_user'))

    queryset_list = queryset_list.order_by('-acctstartdate')
    paginator = Paginator(queryset_list, 50)
    page = request.GET.get('page')
    paged_conexoes = paginator.get_page(page)

    context = {
        'cidades': cidades,
        'bairros': bairros,
        'values': request.GET,      
        'choices': choices,  
        'conexoes': paged_conexoes
    }

    return render(request, 'conexoes/index.html', context)

def details(request ):
    print(request.GET['inicio_conexao'])
    return render(request, 'conexoes/details.html')
