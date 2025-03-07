from django.urls import path
from . import views

app_name = "sistemaFFA"

urlpatterns = [
    path("", views.index, name="index"), 
    path("transacoes/", views.transacoes, name="transacoes"),
    path('filtrar_transacoes/', views.filtrar_transacoes, name='filtrar_transacoes'),
    path("transacoes/<int:transacao_id>/editar/", views.editar_transacao, name="editar_transacao"),
    path("transacoes/<int:transacao_id>/deletar/", views.excluir_transacao, name="excluir_transacao"),
    path("transacoes/<int:transacao_id>/ajax", views.ajax_excluir_transacao, name="ajax_excluir_transacao"),
    path("contatos/", views.contatos, name="contatos"),
    path('filtrar_contatos/', views.filtrar_contatos, name='filtrar_contatos'),
    path("contatos/<int:contato_id>/editar/", views.editar_contato, name="editar_contato"),
    path("contatos/<int:contato_id>/deletar/", views.excluir_contato, name="deletar_contato"),
    path("contatos/<int:contato_id>/ajax/", views.ajax_excluir_contato, name="ajax_excluir_contato"),
    path("categorias/", views.categorias, name="categorias"),
    path('filtrar_categorias/', views.filtrar_categorias, name='filtrar_categorias'),
    path("categorias/<int:categoria_id>/editar/", views.editar_categoria, name="editar_categoria"),
    path("categorias/<int:categoria_id>/deletar/", views.deletar_categoria, name="deletar_categoria"),
    path("conta_bancaria/", views.conta_bancaria, name="conta_bancaria"),
    path("conta_bancaria/<int:conta_bancaria_id>/editar/", views.editar_conta_bancaria, name="editar_conta_bancaria"),
    path("conta_bancaria/<int:conta_bancaria_id>/deletar/", views.deletar_conta_bancaria, name="deletar_conta_bancaria"),
]