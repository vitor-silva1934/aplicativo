"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin                              # Importa o módulo necessário para o painel administrativo do Django
from django.conf import settings                              # Importa as configurações do Django, incluindo variáveis como MEDIA_URL e MEDIA_ROOT
from django.conf.urls.static import static                    # Importa a função 'static' que serve arquivos de mídia
from django.urls import path, include                         # Importa os métodos necessários para configurar as URLs do projeto
from produtos import views                                    # Importa as views do app 'produtos'
from django.contrib.auth.views import LoginView, LogoutView   # Importa as views de login e logout do Django
from produtos import views as produtos_views                  # Importa a view de registro do app 'produtos'


# Definindo as rotas (URLs) da aplicação
urlpatterns = [
    path('admin/', admin.site.urls),                                                       # URL para o painel administrativo
    path('produtos/', include('produtos.urls')),                                           # A URL 'produtos/' inclui as URLs do app 'produtos', permitindo acessar suas páginas
    path('login/', LoginView.as_view(template_name='produtos/login.html'), name='login'),  # A URL 'login/' chama a view de login do Django,
    path('logout/', LogoutView.as_view(), name='logout'),                                  # A URL 'logout/' chama a view de logout do Django, que encerra a sessão do usuário
    path('register/', produtos_views.register, name='register'),                           # A URL 'register/' chama uma view personalizada para o registro de novos usuários
    path('', include('produtos.urls')),                                                    # Página inicial (pode ser a de produtos ou outra)
]

# Serve os arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)