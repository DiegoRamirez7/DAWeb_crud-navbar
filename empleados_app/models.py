from django.db import models

# Create your models here.

class Empleados(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=20)
    telefono=models.PositiveBigIntegerField()
    correo=models.CharField(max_length=20)
    direccion=models.CharField(max_length=20)
    puesto= models.CharField(max_length=10)
    fecha=models.DateField()


    def __str__(self):
        return self.codigo