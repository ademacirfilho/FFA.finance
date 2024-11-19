from django.db import models

class Transacao(models.Model):
   descricao = models.CharField(max_length=100) 
   valor = models.DecimalField(max_digits=10, decimal_places=2)
   data = models.DateField()
   tipoPagamento = models.CharField(max_length=30) 
   pago = models.BooleanField()

class Contato(models.Model):
   nome = models.CharField(max_length=100) 
   cpf = models.CharField(max_length=14, blank=True)
   cnpj = models.CharField(max_length=18, blank=True)
   email = models.EmailField(blank=True)
   telefone = models.CharField(max_length=12) 
   data = models.DateField()

class Categoria(models.Model):
   nome = models.CharField(max_length=100) 
   tipo = models.CharField(max_length=100) 
   data = models.DateField()

class ContaBancaria(models.Model):
   nome = models.CharField(max_length=100) 
   tipo = models.CharField(max_length=100) 
   agenciaConta = models.CharField(max_length=5, blank=True) 
   banco = models.CharField(max_length=100, blank=True) 
   numeroConta = models.CharField(max_length=20)