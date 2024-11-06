from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('listar/', views.listar_produtos, name='listar_produtos'),  # URL para listar os produtos
    path('novo/', views.criar_produto, name='criar_produto'),
    path('deletar/<int:produto_id>/', views.deletar_produto, name='deletar_produto'),
]