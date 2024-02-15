from django.urls import path
from . import views
from .views import añadir_socio, listar_socios, borrar_socio, update_contra

urlpatterns = [
    path('añadir_socio/', añadir_socio, name='añadir_socio') , 
    path('listar_socios/', listar_socios, name='listar_socios'),  
    path('borrar_socio/', borrar_socio, name='borrar_socio'),
    path('update_contra/', update_contra, name='update_contra')
]
