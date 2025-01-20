from django.db import models

class Instrumentos(models.Model):
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    adn = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    serie = models.CharField(max_length=50)
