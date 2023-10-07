"""
URL configuration for OnlyPlants project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from OnlyPlants.views import bienvenida
from OnlyPlants.views import inicio_sesion
from nombreapp.views import home, gestionPreferencias
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("bienvenida/", bienvenida),
    path('inicio_sesion/',inicio_sesion),
    path('',home),
    path('crear_cuenta/', views.postUsuario, name='Crearcuenta'),
    path('preferencias/',views.postPreferencias, name='preferencias'),
    path('gestionPreferencias/',gestionPreferencias),
    path("Encuentra_tu_planta/",views.feed)
    #path("crear_cuenta/redirect/",postUsuario, name='postUsuario'),
    #path("", include("nombreapp.urls")),
    #path("usuarios/", index),
]

