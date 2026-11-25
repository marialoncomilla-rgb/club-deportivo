from django import forms
from .models import Jugador

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = [
            "nombre", "apellido", "edad", "posicion", "numero_camiseta",
            "correo", "telefono", "fecha_ingreso", "activo"
        ]
        widgets = {
            "fecha_ingreso": forms.DateInput(attrs={"type": "date"}),
            "activo": forms.CheckboxInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
        self.fields["activo"].widget.attrs["class"] = "form-check-input"

    def clean_nombre(self):
        valor = self.cleaned_data["nombre"].strip()
        if len(valor) < 2:
            raise forms.ValidationError("El nombre debe tener al menos 2 caracteres.")
        return valor.title()

    def clean_apellido(self):
        valor = self.cleaned_data["apellido"].strip()
        if len(valor) < 2:
            raise forms.ValidationError("El apellido debe tener al menos 2 caracteres.")
        return valor.title()

    def clean_telefono(self):
        valor = self.cleaned_data.get("telefono", "").strip()
        if valor and not all(c.isdigit() or c in "+-() " for c in valor):
            raise forms.ValidationError("Ingresa un teléfono válido.")
        return valor
