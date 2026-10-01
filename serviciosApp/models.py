from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    disponibilidad = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

class PrecioServicio(models.Model):
    servicio = models.OneToOneField(
        Servicio,
        on_delete=models.CASCADE
        # Esto conecta ambos modelos, cada servicio tiene un precio
    )
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2
        )
    descuento = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=0.00
        )
    moneda = models.CharField(
        max_length=10, 
        default='CLP'
        )
    observacion = models.CharField(
        max_length=200, 
        blank=True
        )

    def __str__(self):
        return f"{self.servicio.nombre} - ${self.precio}"
