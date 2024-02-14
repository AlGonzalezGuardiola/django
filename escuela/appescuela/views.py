from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Alumno
import pdb

# Create your views here.
@csrf_exempt
def añadir_alumno(request):
    
    string_body = request.body.decode('utf8').replace("'", '"')
    body = json.loads(string_body)

    nuevo_alumno = Alumno(dni=body['dni'], nombre=body['nombre'])
    nuevo_alumno.save()

    response = {"Mensaje": "Alumno añadido correctamente"}
    return JsonResponse(response)

@csrf_exempt
def listar_alumnos(request):
    alumnos = Alumno.objects.values('id', 'nombre', 'dni')
    return JsonResponse({'alumnos': list(alumnos)})

@csrf_exempt
def mi_vista_sin_proteccion_csrf(request):
    return JsonResponse("Esta vista no tiene protección CSRF.")

@csrf_exempt
def borrar_alumno(request):
    
    string_body = request.body.decode('utf8').replace("'", '"')
    body = json.loads(string_body)

    id = body['dni']

    try:
        alumno_borrar = Alumno.objects.get(dni=id)
        alumno_borrar.delete()
    except Exception:
        response2 = {"Mensaje":"Fallo al borrar el alumno"}
        return JsonResponse(response2)
    response = {"Mensaje": "Alumno borrado correctamente"}
    return JsonResponse(response)
