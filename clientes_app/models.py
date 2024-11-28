from django.db import models

# Create your models here.

class Clientes(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=20)
    direccion=models.CharField(max_length=50)
    correo=models.CharField(max_length=50)
    fecha=models.DateField()
    tipo_cliente=models.CharField(max_length=20)
    telefono=models.PositiveIntegerField()


    def __str__(self):
        return self.codigo