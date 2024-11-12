from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm
from django.shortcuts import render, get_object_or_404
from .models import Carrinho, ItemCarrinho
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def pagina_login(request):
    return render(request, 'produtos/pagina_login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('pagina_inicial')  # Redireciona para a página inicial após login
        else:
            messages.error(request, 'Credenciais inválidas')
    return render(request, 'produtos/login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Login automático após registro
            return redirect('pagina_inicial')  # Redireciona para a página inicial após registro
    else:
        form = UserCreationForm()
    return render(request, 'produtos/register.html', {'form': form})

def pagina_inicial(request):
    return render(request, 'produtos/pagina_inicial.html')

def listar_produtos(request):
    query = request.GET.get('q', '')  # Obtém o parâmetro de pesquisa da URL (caso exista)
    
    if query:
        produtos = Produto.objects.filter(nome__icontains=query)  # Filtra produtos pelo nome
    else:
        produtos = Produto.objects.all()  # Caso não haja filtro, retorna todos os produtos
    
    return render(request, 'produtos/listar.html', {'produtos': produtos, 'query': query})


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
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'POST': 
        produto.delete()
        return redirect('listar_produtos')

    context = {'produto': produto}  #Passa as informações do produto para o template de confirmação
    return render(request, 'produtos/confirm_produto_delete.html', context)


def detalhes_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, 'produtos/detalhes_produto.html', {'produto': produto})


def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')  # Redireciona para a página de listagem
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/editar_produto.html', {'form': form, 'produto': produto})


def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    # Obter a quantidade
    quantidade = int(request.POST.get('quantidade', 1))
    
    # Criar ou verificar o carrinho
    carrinho, _ = Carrinho.objects.get_or_create(user=request.user)
    
    # Criar ou verificar o item no carrinho
    item, created = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)
    
    if not created:
        # Se o item já existe no carrinho, atualizar a quantidade
        item.quantidade += quantidade
    else:
        # Se o item é novo, setar a quantidade
        item.quantidade = quantidade
    
    item.save()  # Salvar o item no carrinho
    
    return redirect('visualizar_carrinho')


def visualizar_carrinho(request):
    carrinho, _ = Carrinho.objects.get_or_create(user=request.user)
    itens = carrinho.itens.all()
    total = sum(item.get_total_item_price() for item in itens)
    return render(request, 'produtos/visualizar.html', {'carrinho': carrinho, 'itens': itens, 'total': total})

def remover_item_carrinho(request, item_id):
    # Obtém o item do carrinho pelo ID
    item = get_object_or_404(ItemCarrinho, id=item_id, carrinho__user=request.user)
    
    # Remove o item do carrinho
    item.delete()
    
    # Redireciona de volta para a visualização do carrinho
    return redirect('visualizar_carrinho')
