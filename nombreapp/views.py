from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "nombreapp/index.html")


