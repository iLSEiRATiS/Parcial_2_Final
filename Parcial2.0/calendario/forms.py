from django import forms

from .models import Evento


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ["titulo", "fecha", "descripcion", "categoria"]
        widgets = {"fecha": forms.DateInput(attrs={"type": "date"})}
