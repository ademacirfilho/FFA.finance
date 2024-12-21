from django.shortcuts import render, get_object_or_404, redirect
from django.forms.models import model_to_dict
from .models import Transacao, Contato, Categoria, ContaBancaria, Pagamento, TipoCategoria, Conta
from .forms import TransacaoForm, ContatoForm, CategoriaForm, ContaBancariaForm
from django.contrib.auth.decorators import login_required

def base(request):
    return render(request, "base.html")

def index(request):
    context = {
        "transacoes": Transacao.objects.all(),
    }

    return render(request, "index.html", context)

def usuario(request):
    return render(request, "usuario.html")

def transacoes(request):
    context = {
        "transacoes": Transacao.objects.all(),
    }

    if request.method == "POST":
        form = TransacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transacoes')
        else:
            context["form"] = form
    else:
        context["form"] = TransacaoForm

    return render(request, "transacoes.html", context)

def contatos(request):
    context = {
        "contatos": Contato.objects.all()
    }

    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contatos')
        else:
            context["form"] = form
    else:
        context["form"] = ContatoForm
    
    return render(request, "contatos.html", context)

def categorias(request):
    context = {
        "categorias": Categoria.objects.all()
    }

    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorias')
        else:
            context["form"] = form
    else:
        context["form"] = CategoriaForm

    return render(request, "categorias.html", context)


def conta_bancaria(request):
    context = {
        "contas_bancarias": ContaBancaria.objects.all()
    }

    if request.method == "POST":
        form = ContaBancariaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('conta_bancaria')
        else:
            context["form"] = form
    else:
        context["form"] = ContaBancariaForm

    return render(request, "conta-bancaria.html", context)