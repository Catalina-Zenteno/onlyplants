from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from django.template import loader

#Esto es una vista
def bienvenida(request):
    return HttpResponse("Only Plants")

def inicia_sesión(request):
    return HttpResponse("<p style= 'color: green;'>Inicia sesión</p>")

def intrucciones(request):
    return render(request, "intrucciones.html")
