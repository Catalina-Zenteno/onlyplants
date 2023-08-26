from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

#Esto es una vista
def bienvenida(request):
    return HttpResponse("Only Plants")

def inicia_sesión(request):
    return HttpResponse("<p style= 'color: green;'>Inicia sesión</p>")

def intrucciones(request):
    plantillaExterna= open("C:/Users/Usuario/OnlyPlants/onlyplants-1/nombreapp/templates/intrucciones.html")
    template= Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto= Context()
    documento= template.render(contexto)
    return HttpResponse(documento)
