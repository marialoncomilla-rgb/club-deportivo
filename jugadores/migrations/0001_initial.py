# Generated for the Club Deportivo academic project.
from django.db import migrations, models
import django.core.validators

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Jugador",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=60, verbose_name="Nombre")),
                ("apellido", models.CharField(max_length=60, verbose_name="Apellido")),
                ("edad", models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(80)], verbose_name="Edad")),
                ("posicion", models.CharField(choices=[("ARQ", "Arquero/a"), ("DEF", "Defensa"), ("MED", "Mediocampista"), ("DEL", "Delantero/a")], max_length=3, verbose_name="Posición")),
                ("numero_camiseta", models.PositiveSmallIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)], verbose_name="Número de camiseta")),
                ("correo", models.EmailField(blank=True, max_length=254, verbose_name="Correo electrónico")),
                ("telefono", models.CharField(blank=True, max_length=20, verbose_name="Teléfono")),
                ("fecha_ingreso", models.DateField(verbose_name="Fecha de ingreso")),
                ("activo", models.BooleanField(default=True, verbose_name="Jugador activo")),
                ("creado", models.DateTimeField(auto_now_add=True)),
            ],
            options={"verbose_name": "jugador", "verbose_name_plural": "jugadores", "ordering": ["apellido", "nombre"]},
        ),
    ]
