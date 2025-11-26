from django import forms

from .models import Apunte


class ApunteForm(forms.ModelForm):
    class Meta:
        model = Apunte
        fields = ["titulo", "contenido"]
        widgets = {"contenido": forms.Textarea(attrs={"rows": 4})}
