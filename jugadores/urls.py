from django.urls import path
from . import views

app_name = "jugadores"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("jugadores/", views.lista_jugadores, name="lista_jugadores"),
    path("jugadores/nuevo/", views.crear_jugador, name="crear_jugador"),
    path("jugadores/<int:pk>/", views.detalle_jugador, name="detalle_jugador"),
    path("jugadores/<int:pk>/editar/", views.editar_jugador, name="editar_jugador"),
    path("jugadores/<int:pk>/eliminar/", views.eliminar_jugador, name="eliminar_jugador"),
]