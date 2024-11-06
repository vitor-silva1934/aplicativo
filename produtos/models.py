from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)                                   # O nome do produto pode conter no maximo 100 caracteres
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)              # O valor do produto em decimal com 10 digitos e duas casas decimais
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True)  # Campo para upload do produto

    def __str__(self):
        return self.nome

# Create your models here.
