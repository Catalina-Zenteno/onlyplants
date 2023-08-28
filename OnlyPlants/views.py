from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from django.template import loader

#Esto es una vista
def bienvenida(request):
    return HttpResponse("Only Plants")

def intrucciones(request):
    return render(request, "intrucciones.html")

def inicio_sesion(request):
    return render(request, "inicio_sesion.html")