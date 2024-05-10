from django.db import models

class Producto (models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='producto')
          
    def __str__(self):
        return self.nombre