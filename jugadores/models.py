from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class Jugador(models.Model):
    POSICIONES = [
        ("ARQ", "Arquero/a"),
        ("DEF", "Defensa"),
        ("MED", "Mediocampista"),
        ("DEL", "Delantero/a"),
    ]

    nombre = models.CharField("Nombre", max_length=60)
    apellido = models.CharField("Apellido", max_length=60)
    edad = models.PositiveSmallIntegerField(
        "Edad", validators=[MinValueValidator(5), MaxValueValidator(80)]
    )
    posicion = models.CharField("Posición", max_length=3, choices=POSICIONES)
    numero_camiseta = models.PositiveSmallIntegerField(
        "Número de camiseta",
        unique=True,
        validators=[MinValueValidator(1), MaxValueValidator(99)]
    )
    correo = models.EmailField("Correo electrónico", blank=True)
    telefono = models.CharField("Teléfono", max_length=20, blank=True)
    fecha_ingreso = models.DateField("Fecha de ingreso")
    activo = models.BooleanField("Jugador activo", default=True)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["apellido", "nombre"]
        verbose_name = "jugador"
        verbose_name_plural = "jugadores"

    def clean(self):
        super().clean()
        if self.nombre and not self.nombre.strip():
            raise ValidationError({"nombre": "El nombre no puede estar vacío."})
        if self.apellido and not self.apellido.strip():
            raise ValidationError({"apellido": "El apellido no puede estar vacío."})

    def __str__(self):
        return f"{self.nombre} {self.apellido} — #{self.numero_camiseta}"
