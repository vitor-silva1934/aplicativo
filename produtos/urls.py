from django.urls import path
from . import views

# Lista das URLs mapeadas para views
urlpatterns = [
    path('', views.pagina_login, name='pagina_login'),                                               # Página inicial: tela de login
    path('login/', views.login_view, name='login'),                                                  # URL para realizar login do usuário
    path('register/', views.register, name='register'),                                              # URL para a criação de um novo novos usuários
    path('pagina_inicial/', views.pagina_inicial, name='pagina_inicial'),                            # Página inicial após realizaro login
    path('listar/', views.listar_produtos, name='listar_produtos'),                                  # Lista todos os produtos disponíveis
    path('novo/', views.criar_produto, name='criar_produto'),                                        # Página para criar um novo produto
    path('detalhes/<int:id>/', views.detalhes_produto, name='detalhes_produto'),                     # Detalhes de um produto específico
    path('editar/<int:id>/', views.editar_produto, name='editar_produto'),                           # Página para editar um produto existente
    path('deletar/<int:produto_id>/', views.deletar_produto, name='deletar_produto'),                # Deleta um produto pelo ID
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),  # Adiciona produto ao carrinho
    path('visualizar/', views.visualizar_carrinho, name='visualizar_carrinho'),                      # Exibe o conteúdo do carrinho do usuário
    path('remover_item/<int:item_id>/', views.remover_item_carrinho, name='remover_item_carrinho'),  # Remove um item específico do carrinho
]

# O path no Django é essencial para associar URLs a funções específicas das views
# Ele recebe três parâmetros principais:
# - string da rota ('' para a raiz ou segmentos como 'login/')
# - a função da view correspondente que será executada ao acessar essa URL
# - um nome identificador opcional para a rota, usado para referenciá-la no código
