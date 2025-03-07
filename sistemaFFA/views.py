from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Transacao, Contato, Categoria, ContaBancaria, TipoCategoria, TipoContato, TipoTransacao
from .forms import TransacaoForm, ContatoForm, CategoriaForm, ContaBancariaForm
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Sum
from django.views.decorators.http import require_POST

def base(request):
    return render(request, "sistemaFFA/base.html")

@login_required
def index(request):
    usuario_atual = request.user

    transacoes_usuario = Transacao.objects.filter(user=usuario_atual)

    paginator = Paginator(transacoes_usuario, 6)
    numero_pagina = request.GET.get('pagina')
    transacoes_paginadas = paginator.get_page(numero_pagina)

    receita = Transacao.objects.filter(user=usuario_atual, tipo__nome='Receita').aggregate(Sum('valor'))['valor__sum'] or 0
    despesa = Transacao.objects.filter(user=usuario_atual, tipo__nome='Despesa').aggregate(Sum('valor'))['valor__sum'] or 0

    context = {
        "transacoes": transacoes_paginadas,
        "receita": receita,
        "despesa": despesa,
    }

    return render(request, "sistemaFFA/index.html", context)

@login_required
def transacoes(request):
    usuario_atual = request.user

    if request.method == "POST":
        form = TransacaoForm(request.POST)
        if form.is_valid():
            transacao = form.save(commit=False)
            transacao.user = usuario_atual
            transacao.save()
            return redirect('sistemaFFA:transacoes')
    else:
        form = TransacaoForm()

    transacoes_usuario = Transacao.objects.filter(user=usuario_atual)

    paginator = Paginator(transacoes_usuario, 3)
    numero_pagina = request.GET.get('pagina')
    transacoes_paginadas = paginator.get_page(numero_pagina)

    receita = Transacao.objects.filter(user=usuario_atual, tipo__nome='Receita').aggregate(Sum('valor'))['valor__sum'] or 0
    despesa = Transacao.objects.filter(user=usuario_atual, tipo__nome='Despesa').aggregate(Sum('valor'))['valor__sum'] or 0
    previsto = receita - despesa

    context = {
        "form": form,
        "transacoes": transacoes_paginadas,
        "tipos": TipoTransacao.objects.all(),
        "receita": receita,
        "despesa": despesa,
        "previsto": previsto,
    }

    return render(request, 'sistemaFFA/transacoes.html', context) 

@login_required
@require_POST
def criar_transacao_ajax(request):
    usuario_atual = request.user
    form = TransacaoForm(request.POST)
    if form.is_valid():
        transacao = form.save(commit=False)
        transacao.user = usuario_atual
        transacao.save()
        
        receita = Transacao.objects.filter(user=usuario_atual, tipo__nome='Receita').aggregate(Sum('valor'))['valor__sum'] or 0
        despesa = Transacao.objects.filter(user=usuario_atual, tipo__nome='Despesa').aggregate(Sum('valor'))['valor__sum'] or 0
        previsto = receita - despesa

        context = {
            'status': 'success',
            'receita': receita,
            'despesa': despesa,
            'previsto': previsto,
        }
        return JsonResponse(context)
    else:
        return JsonResponse({'status': 'error', 'errors': form.errors})

@login_required
def filtrar_transacoes(request):
    tipo_nome = request.GET.get('tipo_nome')
    numero_pagina = request.GET.get('pagina', 1)

    if tipo_nome == "Todas":
        transacoes_filtradas = Transacao.objects.all()
    else:
        transacoes_filtradas = Transacao.objects.filter(tipo__nome=tipo_nome)

    paginator = Paginator(transacoes_filtradas, 3)
    transacoes_paginadas = paginator.get_page(numero_pagina)

    html = render_to_string('sistemaFFA/partials/_transacoes.html', {'transacoes': transacoes_paginadas})
    context = {'status': 'success', 'html': html, 'tipo_nome': tipo_nome}
    return JsonResponse(context)

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
            return redirect('sistemaFFA:transacoes')
        else:
            context["form"] = form

    return render(request, "sistemaFFA/editar_transacao.html", context)

def excluir_transacao(request, transacao_id):
    transacao = get_object_or_404(Transacao, pk=transacao_id)
    return render(request, 'sistemaFFA/deletar_transacao.html', {'transacao': transacao})

@login_required
def ajax_excluir_transacao(request, transacao_id):
    transacao = get_object_or_404(Transacao, pk=transacao_id)
    if request.method == 'POST':
        transacao_id = transacao.id
        transacao.delete()
        return JsonResponse({'status': 'success', 'transacao_id': transacao_id})

    return render(request, "sistemaFFA/partials/_deletar_transacao.html", {'transacao': transacao, 'status': 'error'}) 

@login_required
def contatos(request):
    usuario_atual = request.user
    
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            contatos = form.save(commit=False)
            contatos.user = usuario_atual
            contatos.save()
            return redirect('sistemaFFA:contatos')
    else:
        form = ContatoForm()

    contatos_usuario = Contato.objects.filter(user=usuario_atual)

    deve_para_mim = Transacao.objects.filter(user=usuario_atual, tipo__nome='Receita').aggregate(Sum('valor'))['valor__sum'] or 0
    eu_devo = Transacao.objects.filter(user=usuario_atual, tipo__nome='Despesa').aggregate(Sum('valor'))['valor__sum'] or 0

    paginator = Paginator(contatos_usuario, 3)
    numero_pagina = request.GET.get('pagina')
    contatos_paginados = paginator.get_page(numero_pagina)

    context = {
        "form": form,
        "contatos": contatos_paginados,
        "deve_para_mim": deve_para_mim,
        "eu_devo": eu_devo,
        "tipos": TipoContato.objects.all()
    }
    
    return render(request, "sistemaFFA/contatos.html", context)

@login_required
def filtrar_contatos(request):
    tipo_nome = request.GET.get('tipo_nome')
    numero_pagina = request.GET.get('pagina', 1)

    if tipo_nome == "Todos":
        contatos_filtrados = Contato.objects.all()
    else:
        contatos_filtrados = Contato.objects.filter(tipo__nome=tipo_nome)

    paginator = Paginator(contatos_filtrados, 3)
    contatos_paginados = paginator.get_page(numero_pagina)

    html = render_to_string('sistemaFFA/partials/_contatos.html', {'contatos': contatos_paginados})
    context = {'status': 'success', 'html': html, 'tipo_nome': tipo_nome}
    return JsonResponse(context)

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
            return redirect('sistemaFFA:contatos')
        else:
            context["form"] = form

    return render(request, "sistemaFFA/editar_contato.html", context)

def excluir_contato(request, contato_id):
    contato = get_object_or_404(Contato, pk=contato_id)
    return render(request, 'sistemaFFA/deletar_contato.html', {'contato': contato})

@login_required
def ajax_excluir_contato(request, contato_id):
    contato = get_object_or_404(Contato, pk=contato_id)
    if request.method == 'POST':
        contato_id = contato.id
        contato.delete()
        return JsonResponse({'status': 'success', 'contato_id': contato_id})

    return render(request, "sistemaFFA/partials/_deletar_contato.html", {'contato': contato, 'status': 'error'})

@login_required
def categorias(request):
    usuario_atual = request.user

    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categorias = form.save(commit=False)
            categorias.user = usuario_atual
            categorias.save()
            return redirect('sistemaFFA:categorias')
    else:
        form = CategoriaForm()

    categorias_usuario = Categoria.objects.filter(user=usuario_atual)

    paginator = Paginator(categorias_usuario, 5)
    numero_pagina = request.GET.get('pagina')
    categorias_paginadas = paginator.get_page(numero_pagina)

    context = {
        "form": form,
        "categorias": categorias_paginadas,
        "tipos": TipoCategoria.objects.all()
    }

    return render(request, "sistemaFFA/categorias.html", context)

@login_required
def filtrar_categorias(request):
    tipo_nome = request.GET.get('tipo_nome')
    numero_pagina = request.GET.get('pagina', 1)

    if tipo_nome == "Todas":
        categorias_filtradas = Categoria.objects.all()
    else:
        categorias_filtradas = Categoria.objects.filter(tipo__nome=tipo_nome)

    paginator = Paginator(categorias_filtradas, 5)
    categorias_paginadas = paginator.get_page(numero_pagina)

    html = render_to_string('sistemaFFA/partials/_categorias.html', {'categorias': categorias_paginadas})
    context = {'status': 'success', 'html': html, 'tipo_nome': tipo_nome}
    return JsonResponse(context)

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
            return redirect('sistemaFFA:categorias')
        else:
            context["form"] = form

    return render(request, "sistemaFFA/editar_categoria.html", context)

@login_required
def deletar_categoria(request, categoria_id):
    context = {
        "categorias": get_object_or_404(Categoria, pk=categoria_id)
    }

    if request.method == 'POST':
        context["categorias"].delete()
        return redirect('sistemaFFA:categorias')
    else:
        return render(request, "sistemaFFA/deletar_categoria.html", context)


@login_required
def conta_bancaria(request):
    usuario_atual = request.user

    if request.method == "POST":
        form = ContaBancariaForm(request.POST)
        if form.is_valid():
            conta_bancaria = form.save(commit=False)
            conta_bancaria.user = usuario_atual
            conta_bancaria.save()
            return redirect('sistemaFFA:conta_bancaria')
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

    return render(request, "sistemaFFA/conta_bancaria.html", context)

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
            return redirect('sistemaFFA:conta_bancaria')
        else:
            context["form"] = form

    return render(request, "sistemaFFA/editar_conta_bancaria.html", context)

@login_required
def deletar_conta_bancaria(request, conta_bancaria_id):
    context = {
        "contas_bancarias": get_object_or_404(ContaBancaria, pk=conta_bancaria_id)
    }

    if request.method == 'POST':
        context["contas_bancarias"].delete()
        return redirect('sistemaFFA:conta_bancaria')
    else:
        return render(request, "sistemaFFA/deletar_conta_bancaria.html", context)