from django.db import models


class Monedas(models.Model):
    codigo = models.CharField(max_length=3, unique=True)
    nombre = models.CharField(max_length=50)
    simbolo = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
    
class Ubicaciones(models.Model):
    nombre = models.CharField(max_length=100)
    
    
class Estados(models.Model):
    nombre = models.CharField(max_length=50)