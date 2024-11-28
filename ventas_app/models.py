from django.db import models

# Create your models here.

class Ventas(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    id_cliente = models.CharField(max_length=6)
    fecha=models.DateField()
    total_venta=models.PositiveIntegerField()
    id_producto=models.CharField(max_length=20)
    id_empleado= models.CharField(max_length=6)
    estatus = models.CharField(max_length=50, default='activo')  # Ejemplo de valor predeterminado


    def __str__(self):
        return self.codigo