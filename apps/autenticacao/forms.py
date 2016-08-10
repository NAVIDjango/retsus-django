from django import forms


class FormAutenticacao(forms.Form):
    cpf = forms.CharField(max_length=100)
    senha = forms.CharField(max_length=100)
