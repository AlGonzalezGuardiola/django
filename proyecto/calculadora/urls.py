from django.contrib import admin
from django.urls import path
from .views import mi_vista_sin_proteccion_csrf
from . import views

urlpatterns = [
    path('', views.index),
    path('sumar/<int:op1>/<int:op2>', views.add),
    path('restar/<int:op1>/<int:op2>', views.sub),
    path('multiplicar/<int:op1>/<int:op2>', views.multi),
    path('dividir/<int:op1>/<int:op2>', views.div),
    path('mi-vista-sin-csrf/', mi_vista_sin_proteccion_csrf, name='mi_vista_sin_proteccion_csrf')

]