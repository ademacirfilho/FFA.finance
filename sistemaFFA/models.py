from django.db import models

class Pagamento(models.Model):
   tipoPagamento = models.CharField(max_length=20)

   def __str__(self):
      return self.tipoPagamento

   
class Contato(models.Model):
   nome = models.CharField(max_length=100) 
   cpf_cnpj = models.CharField(max_length=18, blank=True)
   email = models.EmailField(blank=True)
   telefone = models.CharField(max_length=12) 
   data = models.DateField()

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

   def __str__(self):
      return self.nome

class Transacao(models.Model):
   descricao = models.CharField(max_length=100) 
   valor = models.DecimalField(max_digits=10, decimal_places=2)
   data = models.DateField()
   tipoPagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE)
   categoriaNome = models.ForeignKey(Categoria, on_delete=models.CASCADE)
   contatoNome = models.ForeignKey(Contato, on_delete=models.CASCADE)
   pago = models.BooleanField()

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

   def __str__(self):
      return self.nome