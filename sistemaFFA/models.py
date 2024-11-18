from django.db import models

class Transacao(models.Model):
   descricao = models.CharField(max_length=100)  # Corrigido max_lenght para max_length
   valor = models.DecimalField(max_digits=10, decimal_places=2)
   data = models.DateField()
   tipoPagamento = models.CharField(max_length=30)  # Corrigido max_lenght para max_length
   pago = models.BooleanField()

class Contato(models.Model):
   nome = models.CharField(max_length=100)  # Corrigido max_lenght para max_length
   cpf = models.CharField(max_length=14)
   cnpj = models.CharField(max_length=18)
   email = models.EmailField()
   telefone = models.CharField(max_length=12)  # Corrigido max_lenght para max_length
   data = models.DateField()

class Categoria(models.Model):
   nome = models.CharField(max_length=100)  # Corrigido max_lenght para max_length
   tipo = models.CharField(max_length=100)  # Corrigido max_lenght para max_length
   data = models.DateField()

class ContaBancaria(models.Model):
   nome = models.CharField(max_length=100)  # Corrigido max_lenght para max_length
   tipo = models.CharField(max_length=100)  # Corrigido max_lenght para max_length
   agenciaConta = models.CharField(max_length=5)  # Corrigido max_lenght para max_length
   banco = models.CharField(max_length=100)  # Corrigido max_lenght para max_length
   numeroConta = models.CharField(max_length=20)
