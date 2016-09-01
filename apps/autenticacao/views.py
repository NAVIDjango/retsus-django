# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from .forms import FormAutenticacao, FormAlterarSenha, FormAlterarEmail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView


# View de login
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
                    messages.warning(request, 'O usuário nao está ativo!')
            else:
                messages.error(request, 'Usuário ou senha incorretos.')
        else:
            print "Não está ok :("

    return render(request, 'autenticacao/login.html')


# View destinada ao login dos usuários que tentam acessar uma página sem está logado
def pagina_de_login_obrigatorio(request):
    logout(request)
    redirect_to = request.POST.get('next', request.GET.get('next', '/'))

    if request.method == 'POST':
        form = FormAutenticacao(request.POST)
        # Validando se o formulário está correto
        if form.is_valid():
            # Autenticando o usuário
            user = authenticate(username=form.cleaned_data['cpf'], password=form.cleaned_data['senha'])

            # Verificando se a autenticação obteve sucesso
            if user is not None:
                # Verificando se o usuário está ativo
                if user.is_active:
                    login(request, user)
                    return redirect(redirect_to)
                else:
                    messages.warning(request, 'O usuário na está ativo!')
            else:
                messages.error(request, 'Usuário ou senha incorretos.')

    return render(request, 'autenticacao/login.html', {'next': redirect_to})


@login_required()
def sair_do_sistema(request):
    logout(request)
    return redirect('autenticacao:pagina_de_login')


@login_required()
def pagina_index(request):
    return render(request, 'index.html')


@login_required()
def pagina_perfil(request):
    return render(request, 'autenticacao/perfil.html')


@login_required()
def alterar_email(request):
    form = FormAlterarEmail(request.POST or None)
    if form.is_valid():
        u = request.user
        u.email = form.cleaned_data['email_novo']
        u.save()
    return render(request, 'autenticacao/perfil.html')

@login_required()
def alterar_senha(request):
    form = FormAlterarSenha(request.POST or None)
    if form.is_valid():
        u = request.user
        # if form.cleaned_data['senha_antiga'] == u.password:
        # if form.cleaned_data['senha_nova'] == form.cleaned_data['confirmar_senha_nova']:
        u.set_password(form.cleaned_data['senha_nova'])
        u.save()
    messages.error(request, 'Tem nada no campo, boy. Porra é isso?')
    return render(request, 'autenticacao/perfil.html')


#jeito muito bom, mas nao sei como editar os campos do form
# class UsuarioUpdate(LoginRequiredMixin, UpdateView):
#     #form_class = FormEmail
#     model = User
#     fields = ['email', ]
#     template_name = 'autenticacao/perfil.html'
#     success_url = reverse_lazy('autenticacao:alterar_email')
#
#     def get_object(self, queryset=None):
#         return self.request.user
