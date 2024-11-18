from django.shortcuts import render

def base(request):
    return render(request, "base.html")

def index(request):
    return render(request, "index.html")

def usuario(request):
    return render(request, "usuario.html")

def transacoes(request):
    return render(request, "transacoes.html")

def categorias(request):
    return render(request, "categorias.html")

def conta_bancaria(request):
    return render(request, "conta-bancaria.html")

def contatos(request):
    return render(request, "contatos.html")
