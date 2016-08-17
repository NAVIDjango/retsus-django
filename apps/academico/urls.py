from django.conf.urls import url
from .views import cadastro_aluno

urlpatterns = [
    url(r'^$', cadastro_aluno, name='cadastro_aluno'),
]
