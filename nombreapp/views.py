from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse
from .models import Usuario

# Create your views here.
def home(request):
    usuariosListados=Usuario.objects.all()
    return render(request, "gestionUsuarios.html")

