from django.contrib import admin
from .models import Transacao, TipoTransacao, TipoContato, TipoCategoria, Contato, Categoria, ContaBancaria, Pagamento, Conta

admin.site.register(Transacao)
admin.site.register(TipoTransacao)
admin.site.register(Contato)
admin.site.register(TipoContato)
admin.site.register(Categoria)
admin.site.register(TipoCategoria)
admin.site.register(ContaBancaria)
admin.site.register(Pagamento)
admin.site.register(Conta)