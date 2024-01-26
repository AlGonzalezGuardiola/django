from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return HttpResponse("Hola, mundo. Estás en la página de inicio de tu app llamada calculadora.")
@csrf_exempt
def add(request, op1, op2):
    return HttpResponse(op1+op2)
@csrf_exempt
def sub(request, op1, op2):
    return HttpResponse(op1-op2)
@csrf_exempt
def multi(request, op1, op2):
    return HttpResponse(op1*op2)
@csrf_exempt
def div(request, op1, op2):
    try:
        result = op1/op2
    except ZeroDivisionError:
        result = "No division by zero allowed!"
    return HttpResponse(result)


def mi_vista_sin_proteccion_csrf(request):
    # Tu lógica de vista aquí
    return HttpResponse("Esta vista no tiene protección CSRF.")