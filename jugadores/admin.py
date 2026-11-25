from django.contrib import admin
from .models import Jugador

@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "numero_camiseta", "posicion", "activo")
    search_fields = ("nombre", "apellido")
    list_filter = ("posicion", "activo")
