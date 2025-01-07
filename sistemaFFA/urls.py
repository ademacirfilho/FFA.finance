from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("usuario/", views.usuario, name="usuario"),
    path("transacoes/", views.transacoes, name="transacoes"),
    path("transacoes/<int:transacao_id>/editar/", 
         views.editar_transacao, 
         name="editar_transacao"),
    path("transacoes/<int:transacao_id>/deletar/", 
         views.deletar_transacao, 
         name="deletar_transacao"),
    path("contatos/", views.contatos, name="contatos"),
    path("categorias/", views.categorias, name="categorias"),
    path("conta_bancaria/", views.conta_bancaria, name="conta_bancaria")
]