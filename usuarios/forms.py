from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User

class CadastroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", 'email', 'cpf', 'telefone', 'avatar']

class UsuarioChangeForm(UserChangeForm):
    password = None
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", 'email', 'cpf', 'telefone', 'avatar']