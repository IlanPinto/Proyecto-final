from django.urls import path
from MiApp.views import mostrar_entrenadores, mostrar_jugadores, mostrar_torneos
urlpatterns = [
    path('jugadores/', mostrar_jugadores),
    path('entrenadores/', mostrar_entrenadores),
    path('torneos/', mostrar_torneos),
]
