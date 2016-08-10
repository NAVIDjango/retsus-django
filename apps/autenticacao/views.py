# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from .forms import FormAutenticacao


def pagina_de_login(request):
    if request.method == 'POST':
        logout(request)
        form = FormAutenticacao(request.POST)

        # Validando se o formulário está correto
        if form.is_valid():
            print "O Form está ok!"
        else:
            print "Não está ok :("
    return render(request, 'autenticacao/login.html')
