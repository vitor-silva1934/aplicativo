from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm

def pagina_inicial(request):
    return render(request, 'produtos/pagina_inicial.html')

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar.html', {'produtos': produtos})

def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
        
    return render(request, 'produtos/criar.html', {'form': form})

def deletar_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    produto.delete()
    return redirect('listar_produtos')

