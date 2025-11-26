from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EventoForm
from .models import Evento


@login_required
def lista_eventos(request):
    eventos = Evento.objects.filter(usuario=request.user)
    return render(request, "calendario/lista.html", {"eventos": eventos})


@login_required
def crear_evento(request):
    if request.method == "POST":
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.usuario = request.user
            evento.save()
            messages.success(request, "Evento creado.")
            return redirect("eventos")
    else:
        form = EventoForm()
    return render(request, "calendario/form.html", {"form": form, "titulo": "Nuevo evento"})


@login_required
def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk, usuario=request.user)
    if request.method == "POST":
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            messages.success(request, "Evento actualizado.")
            return redirect("eventos")
    else:
        form = EventoForm(instance=evento)
    return render(request, "calendario/form.html", {"form": form, "titulo": "Editar evento"})


@login_required
def eliminar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk, usuario=request.user)
    if request.method == "POST":
        evento.delete()
        messages.info(request, "Evento eliminado.")
        return redirect("eventos")
    return render(request, "calendario/confirmar_eliminar.html", {"evento": evento})
