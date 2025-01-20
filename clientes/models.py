from django.db import models


class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.CharField(max_length=50)
    codigo_comuna = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=False)