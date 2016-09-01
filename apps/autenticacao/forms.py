from django import forms
from .models import User


class FormAutenticacao(forms.Form):
    cpf = forms.CharField(max_length=100)
    senha = forms.CharField(max_length=100)


class FormAlterarEmail(forms.Form):
    email_antigo = forms.CharField(max_length=100)
    email_novo = forms.CharField(max_length=100)


class FormAlterarSenha(forms.Form):
    senha_antiga = forms.CharField(max_length=100)
    senha_nova = forms.CharField(max_length=100)
    confirmar_senha_nova = forms.CharField(max_length=100)


class FormEmail(forms.Form):
    model = User
    fields = ['email', ]
    email = forms.CharField(label="Email: ", max_length=200)
