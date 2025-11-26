from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from api_libros.models import Libro
from galeria.models import Foto
from informes.models import Reporte
from shop.models import Producto
from tareas.models import Tarea
from tareas_cbv.models import TareaCBV
from .forms import RegistroForm


def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado, ahora podes ingresar.")
            return redirect("login")
    else:
        form = RegistroForm()
    return render(request, "cuentas/registro.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/panel/")
        messages.error(request, "Credenciales invalidas.")
    return render(request, "cuentas/login.html")


def logout_view(request):
    logout(request)
    messages.info(request, "Sesion cerrada.")
    return redirect("home")


@login_required
def panel(request):
    stats = {
        "tareas_fbv": Tarea.objects.count(),
        "tareas_cbv": TareaCBV.objects.count(),
        "reportes": Reporte.objects.count(),
        "fotos": Foto.objects.count(),
        "libros": Libro.objects.count(),
        "productos": Producto.objects.count(),
    }
    carrito_items = sum(request.session.get("carrito", {}).values())
    return render(request, "cuentas/panel.html", {"stats": stats, "carrito_items": carrito_items})
