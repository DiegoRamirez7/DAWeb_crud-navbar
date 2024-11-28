from django.db import models

# Create your models here.

class Categorias(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=20)
    descripcion=models.CharField(max_length=20)
    fecha=models.DateField()
    activo=models.CharField(max_length=20)
    prioridad= models.CharField(max_length=10)
    numc=models.PositiveIntegerField()
    
    def __str__(self):
        return self.codigo