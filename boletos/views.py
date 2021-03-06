from django.shortcuts import redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import MkBoletosGerados
from datetime import datetime
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from math import floor

# Create your views here.
@login_required
def index(request):
    return render(request, 'boletos/index.html')

@login_required
def search(request):
    query_list = MkBoletosGerados.objects.all()
    
    # if 'username' in request.GET:
    #     username = request.GET['username']
    #     if username:
    #         query_list = query_list.filter(cd_fatura__cd_pessoa__conexoes__contains=username)
    
    if 'numero' in request.GET:
        numero = request.GET.get('numero')
        if numero:
            query_list = query_list.filter(nosso_numero_formatado__contains=numero)
    
    if 'cliente' in request.GET:
        cliente = request.GET.get('cliente')
        if cliente:
            query_list = query_list.filter(cd_fatura__cd_pessoa__nome_razaosocial__icontains=cliente)
    
    liquidado = request.GET.get('liquidado')
    query_list = query_list.filter(cd_fatura__liquidado__exact=liquidado)

    if 'cpf_cnpj' in request.GET:
        cpf_cnpj = request.GET.get('cpf_cnpj')
        if cpf_cnpj:
            query_list = query_list.filter(Q(cd_fatura__cd_pessoa__cpf=cpf_cnpj) | Q(cd_fatura__cd_pessoa__cnpj=cpf_cnpj))

    
    if 'data_inicial' in request.GET:
        data_inicial = request.GET.get('data_inicial')
        
        if data_inicial:
            if 'data_final' in request.GET:
                data_final = request.GET.get('data_final')
                if data_final:
                    query_list = query_list.filter(cd_fatura__data_vencimento__range=[data_inicial, data_final])
                    
                else:
                    query_list = query_list.filter(cd_fatura__data_vencimento__range=[data_inicial, datetime.today().strftime('%Y-%m-%d')])
        elif 'data_final' in request.GET:
                data_final = request.GET.get('data_final')
                if data_final:
                    query_list = query_list.filter(cd_fatura__data_vencimento__lte=data_final)
    
    if 'liquidado' in request.GET:
        liquidado = request.GET.get('liquidado')

    query_list = query_list.order_by('-cd_fatura__data_vencimento')
    paginator = Paginator(query_list, 50)
    page = request.GET.get('page')
    paged_boletos = paginator.get_page(page)

    page_range = paged_boletos.paginator.page_range
    last_page = page_range[-1]
    middle = floor(last_page / 2)

    print('QUERY: ', query_list.query)
    print('MIDDLE: ', middle)

    range_5 = []

    if paged_boletos.number < 3:
        range_5 = range(1,6)
    else:
        range_5 = range(paged_boletos.number - 3, paged_boletos.number + 2)

    context = {
        'values': request.GET,      
        'boletos': paged_boletos,
        'middle': middle,
        'last_page': last_page,
        'range_5': range_5,
        'range_middle': range(paged_boletos.number - 1, paged_boletos.number + 5),
        'range_last': range(last_page - 5, last_page + 1)
    }

    return render(request, 'boletos/index.html', context)

@login_required
def details(request ):
    boleto = MkBoletosGerados.objects.get(pk=request.GET['bcodgeracao'])
    
    str_vencimento = request.GET['vencimento']

    # vencimento = datetime.strptime(str_vencimento, '%d/%m/%Y')

    conexoes_queryset_list = boleto.cd_fatura.cd_pessoa.conexoes.all()

   
    context = {
        'boleto': boleto,
        'conexoes': conexoes_queryset_list,
        'values': request.GET
    }

    return render(request,'boletos/details.html', context)