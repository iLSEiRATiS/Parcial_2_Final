from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import FotoForm
from .models import Foto


def galeria_view(request):
    if request.method == "POST":
        form = FotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Foto subida.")
            return redirect("galeria")
    else:
        form = FotoForm()
    fotos = Foto.objects.all()
    return render(request, "galeria/galeria.html", {"form": form, "fotos": fotos})
