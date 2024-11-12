from django.db import models
from django.contrib.auth.models import User

# Modelo para representar um produto no sistema
class Produto(models.Model):
    nome = models.CharField(max_length=100)                                   # Nome do produto 
    descricao = models.TextField()                                            # Descrição detalhada do produto
    preco = models.DecimalField(max_digits=10, decimal_places=2)              # Preço com 2 casas decimais
    quantidade = models.IntegerField()                                        # Quantidade disponível do produto
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)  # Imagem (opcional), caso não tenha imagim, sera adicionado uma imagem padrão

    def __str__(self):
        return self.nome  # Retorna o nome do produto

# Categorias de produtos
class Categoria(models.Model):
    nome = models.CharField(max_length=50)  # Nome da categoria

    def __str__(self):
        return self.nome  # Retorna o nome da categoria

# Controle de estoque
class Estoque(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE, related_name='estoque')  # Relaciona a um único produto
    quantidade = models.PositiveIntegerField()                                                 # Quantidade de itens em estoque
    data_entrada = models.DateTimeField(auto_now_add=True)                                     # Data de entrada automática

    def __str__(self):
        return f'Estoque de {self.produto.nome}: {self.quantidade} unidades'  # Exibe o estoque do produto

# Carrinho de compras
class Carrinho(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relaciona o carrinho a um usuário
    criado_em = models.DateTimeField(auto_now_add=True)          # Data de criação automática do carrinho
    
    def __str__(self):
        return f"Carrinho de {self.user.username}"  # Exibe o carrinho do usuário

# Itens do carrinho
class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name='itens')  # Relaciona a um carrinho
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)                          # Relaciona o item a um produto
    quantidade = models.PositiveIntegerField(default=1)                                     # Quantidade do produto no carrinho

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome}"  # Exibe a quantidade e o nome do produto
    
    def get_total_item_price(self):
        return self.quantidade * self.produto.preco        # Calcular o valor dos itens no carrinho