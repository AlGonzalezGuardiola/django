from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Usuario
import pdb

@csrf_exempt
def crear_usuario(request):
    
    string_body = request.body.decode('utf8').replace("'", '"')
    body = json.loads(string_body)

    nuevo_usuario = Usuario(username=body['username'], password=body['password'])
    nuevo_usuario.save()

    response = {"Mensaje": "Usuario creado correctamente"}
    return JsonResponse(response)

@csrf_exempt
def update_contra(request):
    string_body = request.body.decode('utf8').replace("'", '"')
    body = json.loads(string_body)

    id = body['id']
    username = body['username']
    password = body['password']

    try:
        m = Usuario.objects.get(id=id)
        #pdb.set_trace()
        m.username=username
        m.password=password
        m.save()
    except Exception:
        response2 = {"Mensaje": "Fallo al actualizar la contraseña"}
        return JsonResponse(response2)
    response = {"Mensaje": "Contraseña actualizada correctamente"}
    return JsonResponse(response)

@csrf_exempt
def borrar_usuario(request):
    
    string_body = request.body.decode('utf8').replace("'", '"')
    body = json.loads(string_body)

    id = body['id']

    try:
        borrado = Usuario.objects.get(id=id)
        borrado.delete()
    except Exception:
        response2 = {"Mensaje":"Fallo al eliminar el usuario"}
        return JsonResponse(response2)
    response = {"Mensaje": "Usuario eliminado correctamente"}
    return JsonResponse(response)

@csrf_exempt
def ver_usuarios(request):
    usuarios = Usuario.objects.values('id', 'username')
    return JsonResponse({'usuarios': list(usuarios)})

@csrf_exempt
def mi_vista_sin_proteccion_csrf(request):
    return JsonResponse("Esta vista no tiene protección CSRF.")


@csrf_exempt
def contar_nombres(request):
    data = json.loads(request.body)
    username = data.get('username')

    posts = Usuario.objects.filter(username = username).count()
    return JsonResponse({"count": posts})

#@csrf_exempt
#def 