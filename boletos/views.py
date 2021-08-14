from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'boletos/index.html')

def search(request):
    return render(request, 'boletos/index.html')