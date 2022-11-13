from django.shortcuts import render
from MiApp.models import Jugadores, Torneos, Entrenadores

# Create your views here.

def mostrar_jugadores(request):
    j1 = Jugadores(nombre="Rafael",apellido="Nadal", edad = 36, nacionalidad = "Espania" )
    return render (request, 'MiApp/tenis.html' , {'jugadores': {j1}})


def mostrar_torneos(request):
    t1 = Torneos(nombre="Roland Garros", pais="Francia", puntos_otorgados = 2000)
    return render (request, 'MiApp/tenis.html' , {'torneos': {t1}})


def mostrar_entrenadores(request):
    e1 = Entrenadores(nombre="Carlos",apellido="Moya", entrenado = "Rafeal Nadal", email = "cmoya@hotmail.com" )
    return render (request, 'MiApp/tenis.html' , {'entrenadores': {e1}})

