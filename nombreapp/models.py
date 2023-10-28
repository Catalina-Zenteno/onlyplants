from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
# Create your models here.

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
    conexion= models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def preferencias(self):
        return "Id usuario: {} Dimensiones: {} Ciclo: {} Riego: {} Requerimiento de agua:{} Periodo de riego: {} flores: {} luz solar: {} medicinal: {} niños: {} mascotas: {} tropical: {} interior: {} nivel de atencion: {}".format(self.conexion, self.dimensiones, self.ciclo, self.riego, self.requerimiento_de_agua, self.periodo_de_riego, self.flores, self.luz_solar, self.fruta, self.medicinal,self.venenoso_humano, self.venenoso_mascota,self.tropical, self.interior, self.nivel_de_atencion)
    def _str_ (self):
        return self.preferencias()
    class Meta:
        verbose_name="Preferencia"
        verbose_name_plural="Preferencias"
        db_table="Preferencia"
        ordering=['conexion']
