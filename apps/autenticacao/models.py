from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UsuarioDadosExtra(models.Model):
    usuario = models.OneToOneField(User, models.CASCADE, related_name='dados_adicionais')
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)
    foto_perfil = models.ImageField(upload_to='avatar/', blank=True, default='/avatar/avatar.jpg')
    nome_completo = models.TextField()

    def __unicode__(self):
        return '%s' % (self.nome_completo)
