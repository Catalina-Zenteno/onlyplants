from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
'''
class usuario(models.Model):
    correo=models.CharField(primary_key=True, name=str)
    usuario=models.CharField(
        max_length = 20,
        )
    contraseña=models.CharField(
        max_length = 20,
    )
    def _str_(self):
        return self.correo, self.usuario, self.contraseña
'''
class Usuario(models.Model):
    nombre=models.CharField(max_length=30)
    #correo=models.CharField(primary_key=True)
    



'''
class preferencias(models.Model):
    muy_pequeño= 'muy pequeño'
    pequeño='pequeño'
    mediano= 'mediano'
    grande= 'grande'
    muy_grande= 'muy grande'
    dimensiones_choices= (
        (muy_pequeño, 'Muy pequeño'),
        (pequeño, 'Pequeño'),
        (mediano, 'Mediano'),
        (grande, 'Grande'),
        (muy_grande, 'Muy grande'),
    )
    dimensiones=models.CharField(choices=dimensiones_choices)
    anual= 'annual'
    bianual='biannual'
    perenne= 'perennial'
    bienal='biennial'
    ciclo_choices= (
        (anual, 'Que viva un año'),
        (bianual, 'Que dura 6 meses'),
        (perenne, 'Que puedad vivir decadas o siglos'),
        (bienal, 'Que vive dos años'),
    )
    ciclo=models.CharField(choices=ciclo_choices)
    frecuente= 'frequent'
    promedio='average'
    minimo= 'minimum'
    nunca='none'
    riego_choices= (
        (frecuente, 'Frecuente'),
        (promedio, 'Promedio'),
        (minimo, 'Minimo'),
        (nunca, 'Nunca'),
    )
    riego=models.CharField(choices=riego_choices)
    mucho= 'mucho'
    regular='regular'
    poco= 'poco'
    nada='nada'
    requerimiento_de_agua_choices= (
        (mucho, 'Mucho'),
        (regular, 'Regular'),
        (poco, 'Poco'),
        (nada, 'Nada'),
    )
    requerimiento_de_agua=models.CharField(choices=requerimiento_de_agua_choices)
    #No estoy segura que estos sean los parametros de la API
    mañana= 'morning' #Ese si o si es correcto
    tarde='afternnon'
    noche= 'evening'
    periodo_de_riego_choices= (
        (mañana, 'Mañana'),
        (tarde, 'Tarde'),
        (noche, 'Noche'),
    )
    periodo_de_riego=models.CharField(choices=periodo_de_riego_choices)
    si= True
    no=False
    flores_choices= (
        (si, 'Sí'),
        (no, 'No'),
    )
    flores=models.CharField(choices=flores_choices)
    sombra= 'full_shade'
    sombra_parcial='part_shade'
    sol_y_sombra= 'sun-part_shade'
    sol='full_sun'
    luz_solar_choices= (
        (sombra, 'Sombra'),
        (sombra_parcial, 'Parcialmente con sombra'),
        (sol_y_sombra, 'Sol y sombra'),
        (sol, 'Sol'),
    )
    luz_solar=models.CharField(choices=luz_solar_choices)
    si= True
    no=False
    fruta_choices= (
        (si, 'Sí'),
        (no, 'No'),
    )
    fruta=models.CharField(choices=fruta_choices)
    si= True
    no=False
    medicinal_choices= (
        (si, 'Sí'),
        (no, 'No'),
    )
    medicinal=models.CharField(choices=medicinal_choices)
    #La pregunta es: ¿Tienes niños pequeños en tu casa?
    si= False #Entonces la planta no puede ser venenosa
    no= True #Entonces no importa que la planta sea venenosa
    venenoso_humano_choices= (
        (si, 'Sí'),
        (no, 'No'),
    )
    venenoso_humano=models.CharField(choices=venenoso_humano_choices)
    #La pregunta es: ¿Tienes mascotas en tu casa?
    si= False #Entonces la planta no puede ser venenosa
    no= True #Entonces no importa que la planta sea venenosa
    venenoso_mascota_choices= (
        (si, 'Sí'),
        (no, 'No'),
    )
    venenoso_mascota=models.CharField(choices=venenoso_mascota_choices)
    si= True
    no=False
    tropical_choices= (
        (si, 'Sí'),
        (no, 'No'),
    )
    tropical=models.CharField(choices=tropical_choices)
    si= True
    no=False
    interior_choices= (
        (si, 'Sí'),
        (no, 'No'),
    )
    interior=models.CharField(choices=interior_choices)
    #No estoy segura que estos sean los parametros de la API
    bajo= 'Low'
    mediano='Medium' #Ese si o si es correcto
    alto= 'High'
    nivel_de_atencion_choices= (
        (bajo, 'Bajo'),
        (mediano, 'Mediano'),
        (alto, 'Alto'),
    )
    nivel_de_atencion=models.CharField(choices=nivel_de_atencion_choices)
    correo= models.ForeingKey(usuario, on_delete=models.CASCADE, db_column='correo')
    def _str_ (self):
        return self.dimensiones, self.ciclo, self.riego, self.requerimiento_de_agua, self.periodo_de_riego, self.flores, self.luz_solar, self.fruta, self.medicinal,self.venenoso_humano, self.venenoso_mascota,self.tropical, self.interior, self.nivel_de_atencion, self.correo
    
'''


        
        


