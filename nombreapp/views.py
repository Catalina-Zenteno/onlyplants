from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse
from .models import Usuario

# Create your views here.
def home(request):
    usuarios=list(Usuario.objects.all())
    return render(request, "gestionUsuarios.html",{"usuarios":usuarios})

