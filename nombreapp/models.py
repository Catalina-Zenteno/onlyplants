from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Usuario(models.Model):
    nombre=models.CharField(max_length=30)
    correo=models.EmailField(default="@gmail.com")
    id=models.AutoField(primary_key=True)
    contraseña=models.CharField(max_length=120)
    def _str_(self):
        return self.nombre, self.correo, self.id, self.contraseña
    


class preferencias(models.Model):
    dimensiones=models.CharField()
    ciclo=models.CharField()
    riego=models.CharField(default='frecuente')
    requerimiento_de_agua=models.CharField(default='mucho')
    periodo_de_riego=models.CharField(default='mañana')
    flores=models.CharField(default='no')
    luz_solar=models.CharField(default='sombra')
    fruta=models.CharField(default='no')
    medicinal=models.CharField(default='no')
    venenoso_humano=models.CharField(default='si')
    venenoso_mascota=models.CharField(default='si')
    tropical=models.CharField(default='no')
    interior=models.CharField(default='no')
    nivel_de_atencion=models.CharField(default='alto')
    conexion= models.ForeignKey(Usuario, default=1, on_delete=models.CASCADE)
    def _str_ (self):
        return self.dimensiones, self.ciclo, self.riego, self.requerimiento_de_agua, self.periodo_de_riego, self.flores, self.luz_solar, self.fruta, self.medicinal,self.venenoso_humano, self.venenoso_mascota,self.tropical, self.interior, self.nivel_de_atencion, self.conexion


        
        


