from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context
from django.shortcuts import render, redirect
from django.template import loader
from nombreapp.models import preferencias
from django.urls import reverse
import urllib.request
import json
from .import funciones_para_filtro
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
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
        id_usuario=request.user.id
        conexion=User.objects.get(id=id_usuario)
        if dimensiones:
            try:
                print(dimensiones)
                print(conexion)
                preferencia= preferencias.objects.create(dimensiones=dimensiones, ciclo=ciclo, riego=riego, requerimiento_de_agua=requerimiento_de_agua,periodo_de_riego=periodo_de_riego,flores=flores,luz_solar=luz_solar,fruta=fruta,medicinal=medicinal,venenoso_humano=venenoso_humano,venenoso_mascota=venenoso_mascota,tropical=tropical,interior=interior,nivel_de_atencion=nivel_de_atencion, conexion=conexion)
                #preferencia= preferencias.objects.create(dimensiones=dimensiones, ciclo=ciclo)
                preferencia.save()
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



def feed(request):
    id_usuario=request.user.id
    conexion=User.objects.get(id=id_usuario)
    nombre=request.user.username
    print(nombre)
    alo=True
    if alo:
        url= urllib.request.Request(f'https://perenual.com/api/species-list?key=sk-yl4e6521da2899f312380')
        url.add_header('user-agent','hola')
        preferencia=funciones_para_filtro.encontrar_preferencias(id_usuario)
        source=urllib.request.urlopen(url).read()
        list_of_data=json.loads(source)
        preferencia=funciones_para_filtro.traduccion(preferencia)
        plantas=funciones_para_filtro.comparar(preferencia, list_of_data)
        #print(plantas)
        for planta in plantas:
            #print(planta)
            if planta['default_image']!= None:
                planta['default_image']=planta['default_image']['medium_url']
            for elemento in planta:
                if type(planta[elemento]) == list:
                    stri=''
                    for el in elemento:
                        stri+=str(el)
                    planta[elemento]=stri
        texto=open(nombre + '.txt','w')
        texto.write(str(plantas))
        texto.close()
        texto3=open(nombre + 'id.txt','w')
        id=0
        texto3.write(str(id))
        texto3.close()
        texto2=open(nombre + 'preferencias.txt','a')
        texto2.close()
    return render(request, 'feed.html')

def base(request):
    id_usuario=request.user.id
    conexion=User.objects.get(id=id_usuario)
    nombre=request.user.username
    texto=open(nombre + '.txt',"r")
    listaaaa=[]
    p=0
    for linea in texto:
        #print(linea)
        listaaaa.append(linea)
    convertir=listaaaa[0]
    texto.close()
    texto3=open(nombre + 'id.txt','r')
    for linea in texto3:
        id=int(linea.strip())
    texto3.close()
    lista1= list(convertir.strip().split("}, {"))
    #print(lista1)
    #print(id, lista1)
    hola=str(lista1[id])+'}}'
    hola = str(hola)
    #print('------------jkjkjkjkjkjk')
    #print(hola)
    lista=list(hola.strip().split(','))
    #print(lista)
    planta={}
    for elemento in lista:
        print(elemento)
        llave,respuesta=elemento.strip().split(":",1)
        planta[llave]=respuesta
    #print(planta)
    texto3=open(nombre + 'id.txt',"w")
    texto3.write(str(id+1))
    texto3.close()
    if request.method=='POST':
        #print('a')
        respuesta = request.POST.get('respuesta', '').lower().replace(' ', '%20')
        print('respuesta')
        if respuesta=='si':
            texto2=open(nombre + 'preferencias.txt','a')
            modelo='{0} : {1} \n'
            texto2.write('----------- \n')
            for elemento in planta:
                texto2.write(modelo.format(elemento, planta[elemento]))
            texto2.close()
        elif respuesta=='no':
            print('no')
    print(planta)
    imagen=planta["'default_image'"][2:-3]
    print(imagen)
    return render(request, "base.html", {'imagen':imagen,'nombre':planta["'common_name'"],"watering":planta["'watering'"],"cycle":planta["'cycle'"],"sunlight":planta["'sunlight'"]})
    #return render(request, 'ups.html')


def home(request):
    return render(request, 'home.html')

def salir(request):
    logout(request)
    return redirect("/")

def MisPreferencias(request):
    nombre=request.user.username
    archivo=open(nombre + 'preferencias.txt','r')
    i=0
    lista=[]
    dic={}
    for linea in archivo:
        if "------" in linea:
            i+=1
        else:
            #print(linea)
            llave1,resultado=linea.strip().split(" :  ")
            llave1=llave1[1:-1]
            if llave1=="default_image":
                resultado=resultado[1:-3]
                print(resultado)
            print(llave1)
            dic[llave1]=resultado
            #print(llave1, dic[llave1])
            if i==2:
                lista.append(dic)
                print(dic)
                dic={}
                i=0
    print(lista)
    contexto={
        "lista":lista
    }
    #print(lista)   
    print(lista[1]["common_name"])     

    return render(request,"MisPreferencias.html",contexto)

@login_required
def inicio_sesion(request):
    return render(request, "inicio_sesion.html")
    