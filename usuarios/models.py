from django.contrib.auth.models import AbstractUser
from django.db import models

class UsuarioPersonalizado(AbstractUser):
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'fecha_nacimiento', 'telefono']

    def __str__(self):
        return self.username