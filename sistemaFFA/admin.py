from django.contrib import admin
from .models import Transacao, Contato, Categoria, ContaBancaria, Pagamento, TipoCategoria, Conta

admin.site.register(Transacao)
admin.site.register(Contato)
admin.site.register(Categoria)
admin.site.register(ContaBancaria)
admin.site.register(Pagamento)
admin.site.register(TipoCategoria)
admin.site.register(Conta)