from django.db import models

class Socio(models.Model):
    dni = models.CharField(max_length=9, unique=True)
    numero_socio = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=30)