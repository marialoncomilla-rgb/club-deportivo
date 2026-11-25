from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import JugadorForm
from .models import Jugador


def inicio(request):
    total_jugadores = Jugador.objects.count()
    jugadores_activos = Jugador.objects.filter(activo=True).count()
    jugadores_inactivos = Jugador.objects.filter(activo=False).count()

    contexto = {
        "total_jugadores": total_jugadores,
        "jugadores_activos": jugadores_activos,
        "jugadores_inactivos": jugadores_inactivos,
    }
    return render(request, "jugadores/inicio.html", contexto)


def lista_jugadores(request):
    query = request.GET.get("q", "").strip()
    posicion = request.GET.get("posicion", "").strip()

    jugadores = Jugador.objects.all()

    if query:
        jugadores = jugadores.filter(
            Q(nombre__icontains=query)
            | Q(apellido__icontains=query)
            | Q(numero_camiseta__icontains=query)
        )

    if posicion:
        jugadores = jugadores.filter(posicion=posicion)

    contexto = {
        "jugadores": jugadores,
        "query": query,
        "posicion_seleccionada": posicion,
        "posiciones": Jugador.POSICIONES,
    }
    return render(request, "jugadores/lista.html", contexto)


def detalle_jugador(request, pk):
    jugador = get_object_or_404(Jugador, pk=pk)
    return render(request, "jugadores/detalle.html", {"jugador": jugador})


def crear_jugador(request):
    if request.method == "POST":
        form = JugadorForm(request.POST)
        if form.is_valid():
            jugador = form.save()
            messages.success(
                request,
                f"Jugador {jugador.nombre} {jugador.apellido} (#{jugador.numero_camiseta}) creado correctamente.",
            )
            return redirect("jugadores:lista_jugadores")
    else:
        form = JugadorForm()

    contexto = {
        "form": form,
        "modo": "crear",
        "titulo": "Registrar nuevo jugador",
        "texto_boton": "Guardar jugador",
    }
    return render(request, "jugadores/formulario.html", contexto)


def editar_jugador(request, pk):
    jugador = get_object_or_404(Jugador, pk=pk)

    if request.method == "POST":
        form = JugadorForm(request.POST, instance=jugador)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f"Datos de {jugador.nombre} {jugador.apellido} (#{jugador.numero_camiseta}) actualizados.",
            )
            return redirect("jugadores:detalle_jugador", pk=jugador.pk)
    else:
        form = JugadorForm(instance=jugador)

    contexto = {
        "form": form,
        "jugador": jugador,
        "modo": "editar",
        "titulo": f"Editar jugador: {jugador.nombre} {jugador.apellido}",
        "texto_boton": "Guardar cambios",
    }
    return render(request, "jugadores/formulario.html", contexto)


def eliminar_jugador(request, pk):
    jugador = get_object_or_404(Jugador, pk=pk)

    if request.method == "POST":
        nombre_completo = f"{jugador.nombre} {jugador.apellido} (#{jugador.numero_camiseta})"
        jugador.delete()
        messages.success(request, f"Jugador {nombre_completo} eliminado correctamente.")
        return redirect("jugadores:lista_jugadores")

    return render(request, "jugadores/confirmar_eliminar.html", {"jugador": jugador})