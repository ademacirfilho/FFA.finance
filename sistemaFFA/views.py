from django.shortcuts import render, get_object_or_404, redirect
from django.forms.models import model_to_dict
from .models import Transacao, Contato, Categoria, ContaBancaria, TipoCategoria
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

def editar_transacao(request, transacao_id):
    transacao = get_object_or_404(Transacao, pk=transacao_id)
    context = {
        "transacoes": Transacao.objects.all(),
        "form": TransacaoForm(instance=transacao)
    }

    if request.method == "POST":
        form = TransacaoForm(request.POST, instance=transacao)
        if form.is_valid():
            form.save()
            return redirect('transacoes')
        else:
            context["form"] = form

    return render(request, "editar_transacao.html", context)

def deletar_transacao(request, transacao_id):
    context = {
        "transacoes": get_object_or_404(Transacao, pk=transacao_id)
    }

    if request.method == 'POST':
        context["transacoes"].delete()
        return redirect('transacoes')
    else:
        return render(request, "deletar_transacao.html", context)

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

def editar_contato(request, contato_id):
    contato = get_object_or_404(Contato, pk=contato_id)
    context = {
        "contatos": Contato.objects.all(),
        "form": ContatoForm(instance=contato)
    }

    if request.method == "POST":
        form = ContatoForm(request.POST, instance=contato)
        if form.is_valid():
            form.save()
            return redirect('contatos')
        else:
            context["form"] = form

    return render(request, "editar_contato.html", context)

def deletar_contato(request, contato_id):
    context = {
        "contatos": get_object_or_404(Contato, pk=contato_id)
    }

    if request.method == 'POST':
        context["contatos"].delete()
        return redirect('contatos')
    else:
        return render(request, "deletar_contato.html", context)

def categorias(request):
    context = {
        "categorias": Categoria.objects.all(),
        "tipo": TipoCategoria.objects.all()
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


def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    context = {
        "categorias": Categoria.objects.all(),
        "form": CategoriaForm(instance=categoria)
    }

    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categorias')
        else:
            context["form"] = form

    return render(request, "editar_categoria.html", context)

def deletar_categoria(request, categoria_id):
    context = {
        "categorias": get_object_or_404(Categoria, pk=categoria_id)
    }

    if request.method == 'POST':
        context["categorias"].delete()
        return redirect('categorias')
    else:
        return render(request, "deletar_categoria.html", context)

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

    return render(request, "conta_bancaria.html", context)

def editar_conta_bancaria(request, conta_bancaria_id):
    conta_bancaria = get_object_or_404(ContaBancaria, pk=conta_bancaria_id)
    context = {
        "contas_bancarias": ContaBancaria.objects.all(),
        "form": ContaBancariaForm(instance=conta_bancaria)
    }

    if request.method == "POST":
        form = ContaBancariaForm(request.POST, instance=conta_bancaria)
        if form.is_valid():
            form.save()
            return redirect('conta_bancaria')
        else:
            context["form"] = form

    return render(request, "editar_conta_bancaria.html", context)

def deletar_conta_bancaria(request, conta_bancaria_id):
    context = {
        "contas_bancarias": get_object_or_404(ContaBancaria, pk=conta_bancaria_id)
    }

    if request.method == 'POST':
        context["contas_bancarias"].delete()
        return redirect('conta_bancaria')
    else:
        return render(request, "deletar_conta_bancaria.html", context)
