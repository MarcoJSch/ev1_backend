from django.db import models
from django.utils import timezone

class Visita(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    motivo = models.TextField()
    hora_entrada = models.DateTimeField(default=timezone.now)
    hora_salida = models.DateTimeField(null=True, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
