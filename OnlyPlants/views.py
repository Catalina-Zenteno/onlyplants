from django.http import HttpResponse

#Esto es una vista
def bienvenida(request):
    return HttpResponse("Only Plants")

def inicia_sesión(request):
    return HttpResponse("<p style= 'color: green;'>Inicia sesión</p>")