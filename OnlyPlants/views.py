from django.http import HttpResponse

#Esto es una vista
def bienvenida(request):
    return HttpResponse("Only Plants")