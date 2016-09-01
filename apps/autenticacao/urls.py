"""retsus_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import pagina_de_login, pagina_index, sair_do_sistema, pagina_de_login_obrigatorio, pagina_perfil, \
    alterar_email, alterar_senha
#UsuarioUpdate

urlpatterns = [
    url(r'^$', pagina_de_login, name='pagina_de_login'),
    url(r'^sair/$', sair_do_sistema, name='sair_do_sistema'),
    url(r'^dashboard/$', pagina_index, name='pagina_index'),
    url(r'^perfil/$', pagina_perfil, name='pagina_perfil'),
    url(r'^login_obrigatorio/', pagina_de_login_obrigatorio, name='login_obrigatorio'),
    url(r'^alterar_email/', alterar_email, name='alterar_email'),
    url(r'^alterar_senha/', alterar_senha, name='alterar_senha'),
    # url(r'^alterar_email/', UsuarioUpdate.as_view(), name='alterar_email'),
]
