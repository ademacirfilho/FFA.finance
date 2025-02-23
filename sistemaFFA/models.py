from django.db import models
from django.conf import settings

class Pagamento(models.Model):
   tipoPagamento = models.CharField(max_length=20)

   def __str__(self):
      return self.tipoPagamento

class TipoContato(models.Model):
   nome = models.CharField(max_length=20)

   def __str__(self):
      return self.nome

class Contato(models.Model):
   nome = models.CharField(max_length=100)
   tipo = models.ForeignKey(TipoContato, on_delete=models.CASCADE)
   cpf_cnpj = models.CharField(max_length=18, blank=True)
   email = models.EmailField(blank=True)
   telefone = models.CharField(max_length=12, blank=True)
   data = models.DateField()
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

   def __str__(self):
      return self.nome

class TipoCategoria(models.Model):
   nome = models.CharField(max_length=30)

   def __str__(self):
      return self.nome

class Categoria(models.Model):
   nome = models.CharField(max_length=100) 
   tipo = models.ForeignKey(TipoCategoria, on_delete=models.CASCADE) 
   data = models.DateField()
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

   def __str__(self):
      return self.nome

class TipoTransacao(models.Model):
   nome = models.CharField(max_length=30)

   def __str__(self):
      return self.nome

class Transacao(models.Model):
   descricao = models.CharField(max_length=100) 
   valor = models.DecimalField(max_digits=10, decimal_places=2)
   data = models.DateField()
   tipo = models.ForeignKey(TipoTransacao, on_delete=models.CASCADE, default=1)
   tipoPagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE)
   categoriaNome = models.ForeignKey(Categoria, on_delete=models.CASCADE)
   contatoNome = models.ForeignKey(Contato, on_delete=models.CASCADE)
   pago = models.BooleanField()
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

   def __str__(self):
      return self.descricao

class Conta(models.Model):
   tipoConta = models.CharField(max_length=30)

   def __str__(self):
      return self.tipoConta

class ContaBancaria(models.Model):
   nome = models.CharField(max_length=100)
   tipoConta = models.ForeignKey(Conta, on_delete=models.CASCADE)
   agenciaConta = models.CharField(max_length=5, blank=True) 
   banco = models.CharField(max_length=100, blank=True) 
   numeroConta = models.CharField(max_length=20)
   saldo = models.DecimalField(max_digits=10, decimal_places=2)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

   def __str__(self):
      return self.nome