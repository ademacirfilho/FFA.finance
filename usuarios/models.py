from django.db import models
from django.contrib.auth.models import AbstractUser

class Empresa(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255)
    pais = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    cnpj = models.CharField(max_length=18, unique=True)

    def __str__(self):
        return self.nome

class User(AbstractUser):
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField(blank=True, null=True)
    empresa = models.OneToOneField(Empresa, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username