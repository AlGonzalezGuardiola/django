from django.db import models

# Create your models here.

'''
Crea una API para una escuela para gestionar alumnos:
Endpoints:
Introducir alumno (POST) (nombre, dni)
Obtener todos los alumnos(GET)
Borrar alumno (POST)
Modelo que se tendria que utilizar: 
Class Libro Atributos (dni, nombre)
'''
class Alumno(models.Model):
    dni = models.CharField(max_length=9, unique=True)
    nombre = models.CharField(max_length=30)