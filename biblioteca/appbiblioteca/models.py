'''
Crea una API para una biblioteca: 
Endpoints:
Introducir libro (POST) (titulo, num.paginas)
Obtener todos los libros de nuestra base de datos (GET)
Borrar libro (POST)
Modelo que se tendria que utilizar: 
Class Libro Atributos (titulo, num.paginas)
'''

from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField()
    num_paginas = models.IntegerField()