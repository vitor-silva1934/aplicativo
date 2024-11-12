from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_login, name='pagina_login'),  # Página inicial será a de login
    path('login/', views.login_view, name='login'),  # URL de login
    path('register/', views.register, name='register'),  # URL de registro
    path('pagina_inicial/', views.pagina_inicial, name='pagina_inicial'),
    path('listar/', views.listar_produtos, name='listar_produtos'),
    path('novo/', views.criar_produto, name='criar_produto'),
    path('detalhes/<int:id>/', views.detalhes_produto, name='detalhes_produto'),
    path('editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('deletar/<int:produto_id>/', views.deletar_produto, name='deletar_produto'),
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('visualizar/', views.visualizar_carrinho, name='visualizar_carrinho'),
     path('remover_item/<int:item_id>/', views.remover_item_carrinho, name='remover_item_carrinho'),
]
