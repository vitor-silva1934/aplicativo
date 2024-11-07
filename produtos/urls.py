from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('listar/', views.listar_produtos, name='listar_produtos'),                   #listar os produtos
    path('novo/', views.criar_produto, name='criar_produto'),                         #Criação do porduto novo
    path('detalhes/<int:id>/', views.detalhes_produto, name='detalhes_produto'),      # Detalhes do produto
    path('editar/<int:id>/', views.editar_produto, name='editar_produto'),            #Editar produto
    path('deletar/<int:produto_id>/', views.deletar_produto, name='deletar_produto'), #Deletar os produtos
]

if settings.DEBUG:
    # Configurações específicas para o modo DEBUG
    pass