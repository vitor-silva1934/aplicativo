from django.shortcuts import render, redirect, get_object_or_404  # Importa funções para renderizar templates e redirecionar
from .models import Produto, Carrinho, ItemCarrinho               # Importa os modelos Produto, Carrinho e ItemCarrinho
from .forms import ProdutoForm                                    # Importa o formulário ProdutoForm
from django.contrib.auth.decorators import login_required         # Importa o decorador para proteger views com login
from django.contrib.auth.forms import UserCreationForm            # Formulário de criação de usuário
from django.contrib import messages                               # Permite exibir mensagens para o usuário

# Criação das funções
# Exibe a página de login
def pagina_login(request):
    return render(request, 'produtos/pagina_login.html')

# Realiza o login do usuário
def login_view(request):
    if request.method == 'POST':                # Verifica se o método HTTP da requisição é POST, ou seja, se o formulário de login foi enviado.
        username = request.POST['username']     # Pega o nome de usuário e a senha informados pelo usuário no formulário de login
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:                    # Se o usuário for autenticado com sucesso a função login do Django é chamada para autenticar o usuário na sessão atual
            login(request, user)                # Autentica e redireciona para a página inicial
            return redirect('pagina_inicial')
        else:
            messages.error(request, 'Credenciais inválidas')  # Exibe erro em caso de login inválido
    return render(request, 'produtos/login.html')

# Registra um novo usuário
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Autentica automaticamente após o registro
            return redirect('pagina_inicial')
    else:
        form = UserCreationForm()
    return render(request, 'produtos/register.html', {'form': form})

# Página inicial após o login
def pagina_inicial(request):
    return render(request, 'produtos/pagina_inicial.html')

# Lista produtos, com opção de pesquisa
def listar_produtos(request):
    query = request.GET.get('q', '')  # Obtém o termo de pesquisa
    if query:
        produtos = Produto.objects.filter(nome__icontains=query)  # Filtra produtos pelo nome
    else:
        produtos = Produto.objects.all()  # Exibe todos os produtos
    return render(request, 'produtos/listar.html', {'produtos': produtos, 'query': query})

# Cria um novo produto
def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/criar.html', {'form': form})

# Deleta um produto pelo ID
def deletar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST': 
        produto.delete()  # Exclui o produto
        return redirect('listar_produtos')
    context = {'produto': produto}  # Passa informações do produto para confirmação
    return render(request, 'produtos/confirm_produto_delete.html', context)

# Exibe detalhes de um produto específico
def detalhes_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, 'produtos/detalhes_produto.html', {'produto': produto})

# Edita um produto existente
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')  # Redireciona para listagem
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/editar_produto.html', {'form': form, 'produto': produto})

# Adiciona um produto ao carrinho
def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    quantidade = int(request.POST.get('quantidade', 1))  # Obtém a quantidade do item
    carrinho, _ = Carrinho.objects.get_or_create(user=request.user)  # Verifica/exclui o carrinho do usuário
    item, created = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)
    if not created:
        item.quantidade += quantidade  # Atualiza a quantidade se o item já existir
    else:
        item.quantidade = quantidade
    item.save()  # Salva o item
    return redirect('visualizar_carrinho')

# Exibe o carrinho e o total de itens
def visualizar_carrinho(request):
    carrinho, _ = Carrinho.objects.get_or_create(user=request.user)
    itens = carrinho.itens.all()
    total = sum(item.get_total_item_price() for item in itens)  # Calcula o total do carrinho
    return render(request, 'produtos/visualizar.html', {'carrinho': carrinho, 'itens': itens, 'total': total})

# Remove um item específico do carrinho
def remover_item_carrinho(request, item_id):
    item = get_object_or_404(ItemCarrinho, id=item_id, carrinho__user=request.user)
    item.delete()  # Exclui o item do carrinho
    return redirect('visualizar_carrinho')