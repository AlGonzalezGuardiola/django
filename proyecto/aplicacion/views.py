from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
# Validate that the api is working
def index(request):
    response={
        "response": "Hola Mundo cojones"
    }
    return JsonResponse(response)