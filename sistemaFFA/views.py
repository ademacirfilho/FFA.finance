from django.shortcuts import render
from .models import Transacao, Contato, Categoria, ContaBancaria, Pagamento, TipoCategoria, Conta

def base(request):
    return render(request, "base.html")

def index(request):
    return render(request, "index.html")

def usuario(request):
    return render(request, "usuario.html")

def transacoes(request):
    context = {
        "transacoes": Transacao.objects.all(),
    }

    return render(request, "transacoes.html", context)

def categorias(request):
    context = {
        "categorias": Categoria.objects.all()
    }

    return render(request, "categorias.html", context)

def contatos(request):
    context = {
        "contatos": Contato.objects.all()
    }
    return render(request, "contatos.html", context)

def conta_bancaria(request):
    return render(request, "conta-bancaria.html")