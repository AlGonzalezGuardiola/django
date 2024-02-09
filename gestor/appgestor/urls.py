from django.urls import path
from . import views
from .views import crear_usuario, borrar_usuario, contar_nombres, ver_usuarios, update_contra, mi_vista_sin_proteccion_csrf

urlpatterns = [

    path('crear_usuario/', crear_usuario, name='crear_usuario'),
    path('borrar_usuario/', borrar_usuario, name='borrar_usuario'),
    path('ver_usuarios/', ver_usuarios, name='ver_usuarios'),
    path('update_contra/', update_contra, name='update_contra'),
    path('contar_nombres/', contar_nombres, name='contar_nombres'),
    path('mi-vista-sin-csrf/', mi_vista_sin_proteccion_csrf, name='mi_vista_sin_proteccion_csrf')
]
