from django.db import models
from django.contrib.auth.models import User

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True) 

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Estoque(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE, related_name='estoque')
    quantidade = models.PositiveIntegerField()
    data_entrada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Estoque de {self.produto.nome}: {self.quantidade} unidades'

class Carrinho(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Carrinho de {self.user.username}"

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome}"
    
    def get_total_item_price(self):
        return self.quantidade * self.produto.preco