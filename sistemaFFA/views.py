from django.shortcuts import render, get_object_or_404, redirect
from django.forms.models import model_to_dict
from django.core.paginator import Paginator
from .models import Transacao, Contato, Categoria, ContaBancaria, TipoCategoria
from usuarios.models import User, Empresa
from .forms import TransacaoForm, ContatoForm, CategoriaForm, ContaBancariaForm, UserForm, EmpresaForm
from django.contrib.auth.decorators import login_required

def base(request):
    return render(request, "base.html")

@login_required
def index(request):
    context = {
        "transacoes": Transacao.objects.all(),
    }

    paginator = Paginator(Transacao.objects.all(), 5)
    numero_pagina = request.GET.get('pagina')
    transacoes_paginadas = paginator.get_page(numero_pagina)

    context["transacoes"] = transacoes_paginadas


    return render(request, "index.html", context)

@login_required
def usuario(request, user_id):
    usuario = User.objects.get(pk=user_id)
    
    context = {
        "usuario": usuario,
        "empresa": usuario.empresa 
    }
    
    return render(request, "usuario.html", context)

@login_required
def editar_usuario(request, user_id):
    usuario = get_object_or_404(User, pk=user_id)
    context = {
        "usuario": usuario,
        "form": UserForm(instance=usuario)
    }

    if request.method == "POST":
        form = UserForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario', user_id)
        else:
            context["form"] = form

    return render(request, "editar_usuario.html", context)

@login_required
def empresa(request):
    context = {
        "empresa": Empresa.objects.all()
    }

    if request.method == "POST":
        form = EmpresaForm(request.POST)
        if form.is_valid():
            empresa = form.save(commit=False)  # Não salva ainda
            empresa.usuario = request.user  # Associa ao usuário logado
            empresa.save()  # Agora salva com o usuário
            return redirect('index')
        else:
            context["form"] = form
    else:
        context["form"] = EmpresaForm()

    return render(request, "usuario.html", context)

@login_required
def editar_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, pk=empresa_id)
    context = {
        "empresa": empresa,
        "form": EmpresaForm(instance=empresa)
    }

    if request.method == "POST":
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context["form"] = form

    return render(request, "editar_empresa.html", context)

@login_required
def deletar_empresa(request, empresa_id):
    context = {
        "empresa": get_object_or_404(Empresa, pk=empresa_id)
    }

    if request.method == 'POST':
        context["empresa"].delete()
        return redirect('index')
    else:
        return render(request, "deletar_empresa.html", context)

@login_required
def transacoes(request):
    usuario_atual = request.user  # Obtém o usuário logado

    if request.method == "POST":
        form = TransacaoForm(request.POST)
        if form.is_valid():
            transacao = form.save(commit=False)  # Não salva no banco ainda
            transacao.user = usuario_atual  # Define o usuário logado
            transacao.save()
            return redirect('transacoes')
    else:
        form = TransacaoForm()  # Criar o formulário corretamente

    # 🔹 Busca todas as transações do usuário no banco de dados
    transacoes_usuario = Transacao.objects.filter(user=usuario_atual)

    # 🔹 Configura a paginação (3 transações por página)
    paginator = Paginator(transacoes_usuario, 3)
    numero_pagina = request.GET.get('pagina')
    transacoes_paginadas = paginator.get_page(numero_pagina)

    context = {
        "form": form,
        "transacoes": transacoes_paginadas,  # 🔹 Agora realmente está pegando os dados do banco!
    }

    return render(request, 'transacoes.html', context)

@login_required
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

@login_required
def deletar_transacao(request, transacao_id):
    context = {
        "transacoes": get_object_or_404(Transacao, pk=transacao_id)
    }

    if request.method == 'POST':
        context["transacoes"].delete()
        return redirect('transacoes')
    else:
        return render(request, "deletar_transacao.html", context)

@login_required
def contatos(request):
    usuario_atual = request.user
    
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            contatos = form.save(commit=False)
            contatos.user = usuario_atual
            contatos.save()
            return redirect('contatos')
    else:
        form = ContatoForm()

    contatos_usuario = Contato.objects.filter(user=usuario_atual)

    paginator = Paginator(contatos_usuario, 3)
    numero_pagina = request.GET.get('pagina')
    contatos_paginados = paginator.get_page(numero_pagina)

    context = {
        "form": form,
        "contatos": contatos_paginados
    }
    
    return render(request, "contatos.html", context)

@login_required
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

@login_required
def deletar_contato(request, contato_id):
    context = {
        "contatos": get_object_or_404(Contato, pk=contato_id)
    }

    if request.method == 'POST':
        context["contatos"].delete()
        return redirect('contatos')
    else:
        return render(request, "deletar_contato.html", context)

@login_required
def categorias(request):
    usuario_atual = request.user

    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categorias = form.save(commit=False)
            categorias.user = usuario_atual
            categorias.save()
            return redirect('categorias')
    else:
        form = CategoriaForm()

    categorias_usuario = Categoria.objects.filter(user=usuario_atual)

    paginator = Paginator(categorias_usuario, 5)
    numero_pagina = request.GET.get('pagina')
    categorias_paginadas = paginator.get_page(numero_pagina)

    context = {
        "tipo": TipoCategoria.objects.all(),
        "form": form,
        "categorias": categorias_paginadas
    }

    return render(request, "categorias.html", context)


@login_required
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

@login_required
def deletar_categoria(request, categoria_id):
    context = {
        "categorias": get_object_or_404(Categoria, pk=categoria_id)
    }

    if request.method == 'POST':
        context["categorias"].delete()
        return redirect('categorias')
    else:
        return render(request, "deletar_categoria.html", context)


@login_required
def conta_bancaria(request):
    usuario_atual = request.user

    if request.method == "POST":
        form = ContaBancariaForm(request.POST)
        if form.is_valid():
            conta_bancaria = form.save(commit=False)
            conta_bancaria.user = usuario_atual
            conta_bancaria.save()
            return redirect('conta_bancaria')
    else:
        form = ContaBancariaForm()

    conta_bancaria_usuario = ContaBancaria.objects.filter(user=usuario_atual)

    paginator = Paginator(conta_bancaria_usuario, 7)
    numero_pagina = request.GET.get('pagina')
    contas_bancarias_paginadas = paginator.get_page(numero_pagina)

    context = {
        "form": form,
        "contas_bancarias": contas_bancarias_paginadas
    }

    return render(request, "conta_bancaria.html", context)

@login_required
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

@login_required
def deletar_conta_bancaria(request, conta_bancaria_id):
    context = {
        "contas_bancarias": get_object_or_404(ContaBancaria, pk=conta_bancaria_id)
    }

    if request.method == 'POST':
        context["contas_bancarias"].delete()
        return redirect('conta_bancaria')
    else:
        return render(request, "deletar_conta_bancaria.html", context)