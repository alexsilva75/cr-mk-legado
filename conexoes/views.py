from django.db.models import query
from django.db.models.aggregates import Sum
from django.db.models.expressions import F, RawSQL
from django.db.models import Q
from django.shortcuts import render
from datetime import datetime
from django.db.models import Count
from calendar import monthrange
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import MkBairros, MkConexoes, MkContratos, MkRadacct
from .models import MkCidades
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
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

@login_required
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
                    queryset_list = queryset_list.filter(acctstartdate__range=[data_inicial, datetime.today().strftime('%Y-%m-%d')])
        elif 'data_final' in request.GET:
                data_final = request.GET['data_final']
                if data_final:
                    queryset_list = queryset_list.filter(acctstartdate__lte=data_final)
    

    
    if 'cpf_cnpj' in request.GET:
        cpf_cnpj = request.GET['cpf_cnpj']
        print('Filtering CPF: ', cpf_cnpj)
        if cpf_cnpj:
            queryset_list = queryset_list.filter(Q(mkconn_user__codcliente__cpf__contains=cpf_cnpj) | Q(mkconn_user__codcliente__cnpj__contains=cpf_cnpj))

    

    user_count = Count('mkconn_user__username')

    queryset_list = queryset_list.values('mkconn_user',
        'mkconn_user__codcliente__nome_razaosocial',
        'mkconn_user__codcliente__cpf',
        'mkconn_user__codcliente__cnpj',
        'mkconn_user__codcliente__codbairro__bairro',
        'mkconn_user__codcliente__codcidade__cidade',
        ).annotate(user_count=user_count)

    print('QUERY: ', queryset_list.query)

    print('QUERYSET_LIST[0]',queryset_list[0])

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


@login_required
def details(request ):
    queryset_list = MkRadacct.objects.all()
    if 'username' in request.GET:
        mkconn_user = request.GET['username']
        if mkconn_user:
            queryset_list = queryset_list.filter(mkconn_user__exact=mkconn_user)

    if 'inicio_conexao' in request.GET:
        inicio_conexao = request.GET['inicio_conexao']
        
        if inicio_conexao:
            if 'fim_conexao' in request.GET:
                fim_conexao = request.GET['fim_conexao']
                if fim_conexao:
                    queryset_list = queryset_list.filter(acctstartdate__range=[inicio_conexao, fim_conexao])
                    
                else:
                    queryset_list = queryset_list.filter(acctstartdate__range=[inicio_conexao, datetime.today().strftime('%Y-%m-%d')])
        elif 'fim_conexao' in request.GET:
                fim_conexao = request.GET['fim_conexao']
                if fim_conexao:
                    queryset_list = queryset_list.filter(acctstartdate__lte=fim_conexao)
    
    if 'vencimento' in request.GET:
        vencimento = request.GET['vencimento']
        print('VENCIMENTO: ', vencimento)
        arr = vencimento.split(sep="-")
        month = arr[1]
        year = arr[0]

        _ , monthdays = monthrange(int(year), int(month))

        if vencimento:
            queryset_list = queryset_list.filter(acctstartdate__range=[f"{year}-{month}-01", f"{year}-{month}-{monthdays}"])

    
    
    print('QUERY: ', queryset_list.query)
    queryset_list = queryset_list.order_by('-acctstartdate')
    paginator = Paginator(queryset_list, 50)
    page = request.GET.get('page')
    paged_conexoes = paginator.get_page(page)

    context = {
       
        'values': request.GET,      

        'conexoes': paged_conexoes
    }
    return render(request, 'conexoes/details.html', context)
