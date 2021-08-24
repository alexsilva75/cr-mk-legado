from django.shortcuts import redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import MkBoletosGerados
from datetime import datetime
from django.db.models import Q
from django.contrib.auth.decorators import login_required

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
        numero = request.GET['numero']
        if numero:
            query_list = query_list.filter(nosso_numero_formatado__contains=numero)
    
    if 'cliente' in request.GET:
        cliente = request.GET['cliente']
        if cliente:
            query_list = query_list.filter(cd_fatura__cd_pessoa__nome_razaosocial__contains=cliente)
    
    liquidado = request.GET.get('liquidado')
    query_list = query_list.filter(cd_fatura__liquidado__exact=liquidado)

    if 'cpf_cnpj' in request.GET:
        cpf_cnpj = request.GET['cpf_cnpj']
        if cpf_cnpj:
            query_list = query_list.filter(Q(cd_fatura__cd_pessoa__cpf=cpf_cnpj) | Q(cd_fatura__cd_pessoa__cnpj=cpf_cnpj))

    
    if 'data_inicial' in request.GET:
        data_inicial = request.GET['data_inicial']
        
        if data_inicial:
            if 'data_final' in request.GET:
                data_final = request.GET['data_final']
                if data_final:
                    query_list = query_list.filter(cd_fatura__data_vencimento__range=[data_inicial, data_final])
                    
                else:
                    query_list = query_list.filter(cd_fatura__data_vencimento__range=[data_inicial, datetime.today().strftime('%Y-%m-%d')])
        elif 'data_final' in request.GET:
                data_final = request.GET['data_final']
                if data_final:
                    query_list = query_list.filter(cd_fatura__data_vencimento__lte=data_final)

    query_list = query_list.order_by('-cd_fatura__data_vencimento')
    paginator = Paginator(query_list, 50)
    page = request.GET.get('page')
    paged_boletos = paginator.get_page(page)


    print('QUERY: ', query_list.query)
    context = {
        'values': request.GET,      
        'boletos': paged_boletos
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