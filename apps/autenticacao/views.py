# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from .forms import FormAutenticacao


def pagina_de_login(request):
    if request.method == 'POST':
        logout(request)
        form = FormAutenticacao(request.POST)

        # Validando se o formulário está correto
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['cpf'], password=form.cleaned_data['senha'])
            # Verificando se a autenticação obteve sucesso
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('autenticacao:pagina_index')

        else:
            print "Não está ok :("

    return render(request, 'autenticacao/login.html')


def pagina_index(request):
    return render(request, 'index.html')
