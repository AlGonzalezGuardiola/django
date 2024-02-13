from django.urls import path
from . import views
from .views import añadir_libro, listar_libros, borrar_libro

urlpatterns = [

    path('añadir_libro/', añadir_libro, name='añadir_libro') , 
    path('listar_libros/', listar_libros, name='listar_libros'),  
    path('borrar_libro/', borrar_libro, name='borrar_libro')
]
