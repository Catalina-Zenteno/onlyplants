from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Template, Context
from .models import Usuario
from django.template import loader
from django.urls import reverse

# Create your views here.
def home(request):
    usuarios=Usuario.objects.all()
    print(usuarios)
    data={"usuarios":usuarios}
    return render(request, "gestionUsuarios.html",data)

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