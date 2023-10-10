from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context
from django.shortcuts import render, redirect
from django.template import loader
from nombreapp.models import Usuario, preferencias
from django.urls import reverse
import urllib.request
import json
from nombreapp.models import Usuario, preferencias
from .import funciones_para_filtro
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout

#Esto es una vista
def bienvenida(request):
    return HttpResponse("Only Plants")



def postUsuario(request):
    
    if request.method=='POST':
        print('a')
        form= UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            return redirect('../preferencias')
    else:
        form= UserCreationForm()
    context= {'form' : form}
    return render(request, 'Crear_cuenta.html',context)
    '''
        nombre = request.POST.get('nombre', '').lower().replace(' ', '%20')
        correo = request.POST.get('correo', '').lower().replace(' ', '%20')
        contraseña= request.POST.get('contraseña', '').lower().replace(' ', '%20')
        if nombre:
            try:
                print(nombre)
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
    '''

def postPreferencias(request):
    if request.method=='POST':
        print('a')
        #nombre= request.POST.get('nombre', '').lower().replace(' ', '%20')
        dimensiones = request.POST.get('dimensiones', '').lower().replace(' ', '%20')
        ciclo = request.POST.get('ciclo', '').lower().replace(' ', '%20')
        riego= request.POST.get('riego', '').lower().replace(' ', '%20')
        requerimiento_de_agua= request.POST.get('requerimiento_de_agua', '').lower().replace(' ', '%20')
        periodo_de_riego= request.POST.get('periodo_de_riego', '').lower().replace(' ', '%20')
        flores= request.POST.get('flores', '').lower().replace(' ', '%20')
        luz_solar= request.POST.get('luz_solar', '').lower().replace(' ', '%20')
        fruta= request.POST.get('fruta', '').lower().replace(' ', '%20')
        medicinal= request.POST.get('medicinal', '').lower().replace(' ', '%20')
        venenoso_humano= request.POST.get('venenoso_humano', '').lower().replace(' ', '%20')
        venenoso_mascota= request.POST.get('venenoso_mascota', '').lower().replace(' ', '%20')
        tropical= request.POST.get('tropical', '').lower().replace(' ', '%20')
        interior= request.POST.get('interior', '').lower().replace(' ', '%20')
        nivel_de_atencion= request.POST.get('nivel_de_atencion', '').lower().replace(' ', '%20')
        conexion= request.POST.get('conexion', '').lower().replace(' ', '%20')
        if dimensiones:
            try:
                print(dimensiones)
                preferencia= preferencias.objects.create(dimensiones=dimensiones, ciclo=ciclo, riego=riego, requerimiento_de_agua=requerimiento_de_agua,periodo_de_riego=periodo_de_riego,flores=flores,luz_solar=luz_solar,fruta=fruta,medicinal=medicinal,venenoso_humano=venenoso_humano,venenoso_mascota=venenoso_mascota,tropical=tropical,interior=interior,nivel_de_atencion=nivel_de_atencion, conexion=conexion)
                #preferencia= preferencias.objects.create(dimensiones=dimensiones, ciclo=ciclo)
                preferencia.save()
                print(preferencia)
                preferencia1=preferencias.objects.all()
                print(preferencia1)
                #registro = preferencias.objects.get(pk=1)
                #print(registro)
                #dimensiones=registro.dimensiones
                #ciclo= registro.ciclo
                #riego= registro.riego
                #requerimiento_de_agua=registro.requerimiento_de_agua
                #periodo_de_riego=registro.periodo_de_riego
                #flores=registro.flores
                #luz_solar=registro.luz_solar
                #fruta= registro.fruta
                #medicinal= registro.medicinal
                #venenoso_humano=registro.venenoso_humano
                #venenoso_mascota=registro.venenoso_mascota
                #tropical=registro.tropical
                #interior=registro.interior
                #nivel_de_atencion=registro.nivel_de_atencion
                #nombre=registro.nombre
                print(dimensiones)
                print(ciclo)
                print(riego)
                print(requerimiento_de_agua)
                print(periodo_de_riego)
                print(flores)
                print(luz_solar)
                print(fruta)
                print(medicinal)
                print(venenoso_humano)
                print(venenoso_mascota)
                print(tropical)
                print(interior)
                print(nivel_de_atencion)
                #print(nombre)
                plantilla=loader.get_template('preferencias.html')
                return HttpResponseRedirect(reverse('preferencias'))
            except Exception as e:
                print('error')
                return render(request, "error.html")
    #return HttpResponse(plantilla.render({},request))
    else:
       return render(request, 'preferencias.html')

'''
def index(request):
    usuario=usuario.objects.all().values()
    context={
        'usuario': usuario,
    }

'''
def feed(request):
    url= urllib.request.Request(f'https://perenual.com/api/species-list?key=sk-CLbk6521e23f71c8f2231')
    url.add_header('user-agent','hola')
    #preferencias=preferencias.objects.get(pk=1)
    preferencias={'dimensiones':'muy_grande',
                  'ciclo':'perenne',
                  'riego':'promedio',
                  'requerimiento_de_agua':'poco',
                  'periodo_de_riego':'noche',
                  'flores':'si',
                  'luz_solar':'sol',
                  'fruta':'no',
                  'medicinal':'no',
                  'venenoso_humano':'no',
                  'venenoso_mascota':'no',
                  'tropical':'no',
                  'interior':'si',
                  'nivel_de_atencion':'alto',
                  }
    source=urllib.request.urlopen(url).read()
    list_of_data=json.loads(source)
    preferencias=funciones_para_filtro.traduccion(preferencias)
    plantas=funciones_para_filtro.comparar(preferencias, list_of_data)
    print(plantas)
    return render(request, "feed.html")


def home(request):
    return render(request, 'home.html')

def salir(request):
    logout(request)
    return redirect("/")

@login_required
def inicio_sesion(request):
    return render(request, "inicio_sesion.html")
    