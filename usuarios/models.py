from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField(
        upload_to="usuarios/avatar/",
        blank=True
    )
    def __str__(self):
        return self.first_name