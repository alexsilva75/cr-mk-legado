from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Você está logado.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuário e/ou senha inválido(s).')
            return redirect('login')

    return render(request, 'accounts/login.html')

def logout(request):
   # print('Logout method: ', request.method )
    if request.method == 'POST':
        print('Logging out......')
        auth.logout(request)
        messages.success(request, 'Você foi desconectado com sucesso.')
        return redirect('login')