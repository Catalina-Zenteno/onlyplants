from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from django.template import loader
#from nombreapp.models import usuario

#Esto es una vista
def bienvenida(request):
    return HttpResponse("Only Plants")

def inicio_sesion(request):
    return render(request, "inicio_sesion.html")
'''
def index(request):
    usuario=usuario.objects.all().values()
    context={
        'usuario': usuario,
    }

'''