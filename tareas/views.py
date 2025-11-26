from django.shortcuts import get_object_or_404, redirect, render

from .forms import TareaForm
from .models import Tarea


def lista_tareas(request):
    tareas = Tarea.objects.all().order_by("-fecha_creacion")
    return render(request, "tareas/lista.html", {"tareas": tareas})


def crear_tarea(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_tareas")
    else:
        form = TareaForm()
    return render(request, "tareas/form.html", {"form": form, "accion": "Crear"})


def editar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == "POST":
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect("lista_tareas")
    else:
        form = TareaForm(instance=tarea)
    return render(request, "tareas/form.html", {"form": form, "accion": "Editar"})


def borrar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == "POST":
        tarea.delete()
        return redirect("lista_tareas")
    return render(request, "tareas/confirmar_borrar.html", {"tarea": tarea})
