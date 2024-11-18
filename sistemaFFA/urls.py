from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("usuario/", views.usuario, name="usuario"),
    path("transacoes/", views.transacoes, name="transacoes"),
    path("contatos/", views.contatos, name="contatos"),
    path("categorias/", views.categorias, name="categorias"),
    path("conta_bancaria/", views.conta_bancaria, name="conta_bancaria")
]