from django.db import models

# Create your models here.

class Productos(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=30)
    fecha=models.DateField()
    precio=models.PositiveIntegerField()
    descripcion=models.CharField(max_length=20)
    categoria= models.CharField(max_length=20)
    stock= models.CharField(max_length=20)



    def __str__(self):
        return self.codigo