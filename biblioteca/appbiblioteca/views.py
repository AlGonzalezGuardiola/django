from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Libro
import pdb

# Create your views here.
@csrf_exempt
def añadir_libro(request):
    
    string_body = request.body.decode('utf8').replace("'", '"')
    body = json.loads(string_body)

    nuevo_libro = Libro(titulo=body['titulo'], num_paginas=body['num_paginas'])
    nuevo_libro.save()

    response = {"Mensaje": "Libro añadido correctamente"}
    return JsonResponse(response)

@csrf_exempt
def listar_libros(request):
    libros = Libro.objects.values('id', 'titulo', 'num_paginas')
    return JsonResponse({'usuarios': list(libros)})

@csrf_exempt
def mi_vista_sin_proteccion_csrf(request):
    return JsonResponse("Esta vista no tiene protección CSRF.")

@csrf_exempt
def borrar_libro(request):
    
    string_body = request.body.decode('utf8').replace("'", '"')
    body = json.loads(string_body)

    id = body['titulo']

    try:
        borrado = Libro.objects.get(titulo=id)
        borrado.delete()
    except Exception:
        response2 = {"Mensaje":"Fallo al borrar el libro"}
        return JsonResponse(response2)
    response = {"Mensaje": "Libro borrado correctamente"}
    return JsonResponse(response)
