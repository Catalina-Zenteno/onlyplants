import urllib.request
import json
from nombreapp.models import preferencias


def pasar_a_diccionario(preferencia_objeto):
    preferencia={}
    preferencia['dimensiones']=preferencia_objeto.dimensiones
    print(preferencia_objeto.dimensiones)
    preferencia['ciclo']=preferencia_objeto.ciclo
    preferencia['riego']=preferencia_objeto.riego
    preferencia['requerimiento_de_agua']=preferencia_objeto.requerimiento_de_agua
    preferencia['periodo_de_riego']=preferencia_objeto.periodo_de_riego
    preferencia['flores']=preferencia_objeto.flores
    preferencia['luz_solar']=preferencia_objeto.luz_solar
    preferencia['fruta']=preferencia_objeto.fruta
    preferencia['medicinal']=preferencia_objeto.medicinal
    preferencia['venenoso_humano']=preferencia_objeto.venenoso_humano
    preferencia['venenoso_mascota']=preferencia_objeto.venenoso_mascota
    preferencia['tropical']=preferencia_objeto.tropical
    preferencia['interior']=preferencia_objeto.interior
    preferencia['nivel_de_atencion']=preferencia_objeto.nivel_de_atencion
    return preferencia

def encontrar_preferencias(id_usuario):
    preferencia_objeto= preferencias.objects.get(id=3)
    print(preferencia_objeto)
    preferencia=pasar_a_diccionario(preferencia_objeto)
    return preferencia

def traduccion(preferencias):
    for p in preferencias:
        if p == 'dimensiones':
            if preferencias['dimensiones']=="muy_pequeño":
                preferencias['dimensiones']=list(range(0,1,1))
            elif preferencias['dimensiones']=='pequeño':
                preferencias['dimensiones']=list(range(2,3,1))
            elif preferencias['dimensiones']=="mediano":
                preferencias['dimensiones']=list(range(3,4,1))
            elif preferencias['dimensiones']=="grande":
                preferencias['dimensiones']=list(range(5,13,1))
            elif preferencias['dimensiones']=="muy_grande":
                preferencias['dimensiones']=list(range(14,100000,1))
        elif p=='ciclo':
            if preferencias['ciclo']=='anual':
                preferencias['ciclo']=="Annual"
            elif preferencias['ciclo']=='bianual':
                preferencias['ciclo']='Biannual'
            elif preferencias['ciclo']=="perenne":
                preferencias['ciclo']='Perennial'
            elif preferencias['ciclo']=='bienal':
                preferencias['ciclo']='Biennial'
        elif p=='riego':
            if preferencias['riego']=='frecuente':
                preferencias['riego']='Frequent'
            elif preferencias['riego']=='promedio':
                preferencias['riego']='Average'
            elif preferencias['riego']=='minimo':
                preferencias['riego']='Minimum'
            elif preferencias['riego']=='nunca':
                preferencias['riego']='None'
        #elif p=='requerimiento_de_agua':
            #if preferencias['requerimiento_de_agua']=='mucho':
        #elif p=='periodo_de_riego':
        elif p=='flores':
            if preferencias['flores']=='si':
                preferencias['flores']=True
            elif preferencias['flores']=='no':
                preferencias['flores']=False
        elif p=='luz_solar':
            if preferencias['luz_solar']=='sombra':
                preferencias['luz_solar']='full shade'
            elif preferencias['luz_solar']=='sombra_parcial':
                preferencias['luz_solar']='part shade'
            elif preferencias['luz_solar']=='sol_y_sombra':
                preferencias['luz_solar']='part sun/part shade'
            elif preferencias['luz_solar']=='sol':
                preferencias['luz_solar']='full sun'
        elif p=='fruta':
            if preferencias['fruta']=='si':
                preferencias['fruta']=True
            elif preferencias['fruta']=='no':
                preferencias['fruta']=False
        elif p=='medicinal':
            if preferencias['medicinal']=='si':
                preferencias['medicinal']=True
            elif preferencias['medicinal']=='no':
                preferencias['medicinal']=False
        elif p=='venenoso_humano':
            if preferencias['venenoso_humano']=='si':
                preferencias['venenoso_humano']=False
            elif preferencias['venenoso_humano']=='no':
                preferencias['venenoso_humano']=True
        elif p=='venenoso_mascota':
            if preferencias['venenoso_mascota']=='si':
                preferencias['venenoso_mascota']=False
            elif preferencias['venenoso_mascota']=='no':
                preferencias['venenoso_mascota']=True
        elif p=='tropical':
            if preferencias['tropical']=='si':
                preferencias['tropical']=True
            elif preferencias['tropical']=='no':
                preferencias['tropical']=False
        elif p=='interior':
            if preferencias['interior']=='si':
                preferencias['interior']=True
            elif preferencias['interior']=='no':
                preferencias['interior']=False
        #elif p=='nivel_de_atencion':
            #if preferencias['nivel_de_atencion']=='bajo':
    return preferencias

def comparar(preferencias, list_of_data):
    plantas=[]
    for planta in list_of_data['data']:
        if  planta['cycle']==preferencias['ciclo']:
            if  planta['watering']==preferencias['riego']:
                #print(preferencias['luz_solar'],"in",planta['sunlight'])
                if preferencias['luz_solar'] in planta['sunlight']:
                    #print("prueba")
                    plantas.append(planta)
                    id=planta['id']
                    url= urllib.request.Request(f'https://perenual.com/api/species/details/'+str(id)+'?key=sk-CLbk6521e23f71c8f2231')
                    url.add_header('user-agent','hola')
                    source=urllib.request.urlopen(url).read()
                    list_of_data2=json.loads(source)
                    #print(list_of_data2)
                    #print(list_of_data2['dimensions']["max_value"])
                    if list_of_data2['dimensions']["max_value"] in preferencias['dimensiones']:
                        if list_of_data2['flowers']==preferencias['flores']:  
                            if list_of_data2['fruits']==preferencias['fruta']:
                                if list_of_data2['medicinal']==preferencias['medicinal']:
                                     if list_of_data2['poisonous_to_humans']==preferencias['venenoso_humano']:
                                        if list_of_data2['poisonous_to_pets']==preferencias['venenoso_mascota']:
                                            if list_of_data2['tropical']==preferencias['tropical']:
                                                if list_of_data2['indoor']==preferencias['interior']:
                                                    plantas.append(list_of_data2)
                
    return plantas


