from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context
from django.shortcuts import render
from django.template import loader
from nombreapp.models import Usuario
from django.urls import reverse

#Esto es una vista
def bienvenida(request):
    return HttpResponse("Only Plants")

def inicio_sesion(request):
    return render(request, "inicio_sesion.html")

def crear_cuenta(request):
    plantilla=loader.get_template('Crear_cuenta.html')
    return HttpResponse(plantilla.render({},request))

def postUsuario(request):
    nombre=request.POST['nombre']
    correo=request.POST['correo']
    contraseña=request.POST['contraseña']
    usuario= Usuario.objects.create(nombre=nombre,correo=correo,contraseña=contraseña)
    usuario.save()
    return HttpResponseRedirect(reverse('getUsuario'))


'''
def index(request):
    usuario=usuario.objects.all().values()
    context={
        'usuario': usuario,
    }

'''