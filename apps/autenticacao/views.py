from django.shortcuts import render


def pagina_de_login(request):
    return render(request, 'autenticacao/login.html')
