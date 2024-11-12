from django.contrib import admin
from .models import Produto
from .models import Categoria
from .models import Estoque
from .models import Carrinho
from .models import ItemCarrinho

admin.site.register(Produto)
admin.site.register(Categoria)
admin.site.register(Estoque)
admin.site.register(Carrinho)
admin.site.register(ItemCarrinho)

# Register your models here.
