from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import MkBoletosGerados
# Create your views here.
def index(request):
    return render(request, 'boletos/index.html')

def search(request):
    query_list = MkBoletosGerados.objects.all()

    if 'numero' in request.GET:
        numero = request.GET['numero']
        if numero:
            query_list = query_list.filter(nosso_numero_formatado__contains=numero)
    
    if 'username' in request.GET:
        username = request.GET['username']
        if username:
            query_list = query_list.filter(username__contains=username)
    
    if 'cliente' in request.GET:
        cliente = request.GET['cliente']
        if cliente:
            query_list = query_list.filter(cd_fatura__cd_pessoa__nome_razaosocial__contains=cliente)

    paginator = Paginator(query_list, 50)
    page = request.GET.get('page')
    paged_boletos = paginator.get_page(page)

    context = {
        'values': request.GET,      
        'boletos': paged_boletos
    }

    return render(request, 'boletos/index.html', context)