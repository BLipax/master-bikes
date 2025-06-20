from django.db import models
from django.conf import settings


class Bicicleta(models.Model):
    TIPO_CHOICES = [
        ('MTB', 'Montaña'),
        ('URB', 'Urbana'),
        ('EBK', 'Eléctrica'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=3, choices=TIPO_CHOICES)
    descripcion = models.TextField()
    disponible_para_venta = models.BooleanField(default=True)
    disponible_para_arriendo = models.BooleanField(default=True)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    precio_arriendo_hora = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    imagen = models.ImageField(upload_to='bicicletas/', null=True, blank=True)

    def __str__(self):
        return self.nombre
    
class Arriendo(models.Model):
        usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        bicicleta = models.ForeignKey(Bicicleta, on_delete=models.CASCADE)
        fecha = models.DateField()
        hora_inicio = models.TimeField()
        hora_fin = models.TimeField()

def __str__(self):
        return f"{self.usuario.username} - {self.bicicleta.nombre} ({self.fecha} {self.hora_inicio}-{self.hora_fin})"
