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


def postUsuario(request):
    if request.method=='POST':
        print('a')
        nombre = request.POST.get('nombre', '').lower().replace(' ', '%20')
        correo = request.POST.get('correo', '').lower().replace(' ', '%20')
        contraseña= request.POST.get('contraseña', '').lower().replace(' ', '%20')
        #nombre=request.POST['nombre'].lower()
        #nombre=nombre.replace(' ','%20')
        if nombre:
            try:
                print(nombre)
                #nombre=request.POST['nombre']
                #correo=request.POST['correo']
                #contraseña=request.POST['contraseña']
                #usuario= Usuario.objects.create(nombre=nombre,correo=correo,contraseña=contraseña)
                usuario= Usuario.objects.create(nombre=nombre, correo=correo, contraseña=contraseña)
                usuario.save()
                usuario1=Usuario.objects.all()
                print(usuario1)
                registro = Usuario.objects.get(pk=21)
                nombre=registro.nombre
                correo= registro.correo
                contraseña= registro.contraseña
                print(nombre)
                print(correo)
                print(contraseña)
                plantilla=loader.get_template('Crear_cuenta.html')
                return HttpResponseRedirect(reverse('Crearcuenta'))
            except Exception as e:
                print('error')
                return render(request, "error.html")
    #return HttpResponse(plantilla.render({},request))
    else:
       return render(request, 'Crear_cuenta.html')



'''
def index(request):
    usuario=usuario.objects.all().values()
    context={
        'usuario': usuario,
    }

'''