from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Socio
import pdb
@csrf_exempt
def añadir_socio(request):
    
    string_body = request.body.decode('utf8').replace("'", '"')
    body = json.loads(string_body)

    nuevo_socio = Socio(nombre=body['nombre'], dni=body['dni'], numero_socio=body['numero_socio'], contraseña = body['contraseña'] )
    nuevo_socio.save()

    response = {"Mensaje": "Socio añadido correctamente"}
    return JsonResponse(response)

@csrf_exempt
def listar_socios(request):
    socios = Socio.objects.values('nombre', 'dni', 'numero_socio')
    return JsonResponse({'Socios': list(socios)})
@csrf_exempt
def borrar_socio(request):
    
    string_body = request.body.decode('utf8').replace("'", '"')
    body = json.loads(string_body)

    id = body['dni']

    try:
        socio_borrar = Socio.objects.get(dni=id)
        socio_borrar.delete()
    except Exception:
        response2 = {"Mensaje":"Fallo al borrar el socio"}
        return JsonResponse(response2)
    response = {"Mensaje": "Socio borrado correctamente"}
    return JsonResponse(response)


@csrf_exempt
def update_contra(request):
    string_body = request.body.decode('utf8').replace("'", '"')
    body = json.loads(string_body)

    numero_socio = body['numero_socio']
    dni = body['dni']
    contraseña = body['contraseña']

    try:
        m = Socio.objects.get(id=id)
        #pdb.set_trace()
        m.numero_socio=numero_socio
        m.dni=dni
        m.contraseña=contraseña
        m.save()
    except Exception:
        response2 = {"Mensaje": "Fallo al actualizar la contraseña"}
        return JsonResponse(response2)
    response = {"Mensaje": "Contraseña actualizada correctamente"}
    return JsonResponse(response)

@csrf_exempt
def mi_vista_sin_proteccion_csrf(request):
    return JsonResponse("Esta vista no tiene protección CSRF.")


