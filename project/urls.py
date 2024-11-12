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
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from produtos import views
from django.contrib.auth.views import LoginView, LogoutView
from produtos import views as produtos_views

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para o painel administrativo
    path('produtos/', include('produtos.urls')),  # Incluindo as URLs do app produtos
    path('login/', LoginView.as_view(template_name='produtos/login.html'), name='login'),  # Login via auth_views
    path('logout/', LogoutView.as_view(), name='logout'),  # Logout padrão do Django
    path('register/', produtos_views.register, name='register'),  # Registro via view personalizada
    path('', include('produtos.urls')),  # Página inicial (pode ser a de produtos ou outra)
]

# Serve os arquivos de mídia durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)