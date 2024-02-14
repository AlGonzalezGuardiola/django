from django.urls import path
from . import views
from .views import añadir_alumno, listar_alumnos, borrar_alumno

urlpatterns = [
    path('añadir_alumno/', añadir_alumno, name='añadir_alumno') , 
    path('listar_alumnos/', listar_alumnos, name='listar_alumnos'),  
    path('borrar_alumno/', borrar_alumno, name='borrar_alumno')
]
