from django.db import models

# Create your models here.

class Proveedores(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=20)
    telefono=models.PositiveBigIntegerField()
    correo=models.CharField(max_length=20)
    direccion=models.CharField(max_length=20)
    principal= models.CharField(max_length=10)
    
    def __str__(self):
        return self.codigo