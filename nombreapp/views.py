from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Template, Context
from .models import Usuario, preferencias
from django.template import loader
from django.urls import reverse

# Create your views here.
def home(request):
    usuarios=Usuario.objects.all()
    #print(usuarios)
    registro = Usuario.objects.get(pk=21)
    data={
        "usuarios": usuarios,
        "nombre":registro.nombre,
        "correo":registro.correo
        }
    return render(request, "gestionUsuarios.html",data)
def gestionPreferencias(request):
    preferencia=preferencias.objects.all()
    print(preferencias)
    #registro = preferencias.objects.get(pk=21)
    data={
        "preferencia": preferencia,
        }
    return render(request, "gestionPreferencias.html",data)
'''
def crear_cuenta(request):
    plantilla=loader.get_template('Crear_cuenta.html')
    return HttpResponse(plantilla.render({},request))
'''
'''
def postUsuario(request):
    #nombre=request.POST['nombre']
    #correo=request.POST['correo']
    #contraseña=request.POST['contraseña']
    #usuario= Usuario.objects.create(nombre=nombre,correo=correo,contraseña=contraseña)
    #usuario.save()
    #plantilla=loader.get_template('Crear_cuenta.html')
    #return HttpResponseRedirect(reverse('getUsuario'))
    #return HttpResponse(plantilla.render({},request))
    return render(request, 'Crear_cuenta.html')
'''