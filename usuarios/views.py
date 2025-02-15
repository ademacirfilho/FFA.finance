from django.shortcuts import render, redirect
from .forms import CadastroForm

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            ## messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('index')
    else:
        form = CadastroForm()
    return render(request, 'cadastro.html', {'form': form})