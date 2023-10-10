from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Template, Context
from .models import Usuario, preferencias
from django.template import loader
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.

def perfil(request, username=None):
    current_user=request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
    else:
        user = current_user
    return render(request, 'perfil.html', {'user':user})

def gestionPreferencias(request):
    preferencia=preferencias.objects.all()
    print(preferencias)
    #registro = preferencias.objects.get(pk=1)
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
def AcercaDeNosotros(request):
    return render(request, 'Acerca_de_nosotros.html')

