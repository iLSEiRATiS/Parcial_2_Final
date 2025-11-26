from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.core.mail import send_mail

from .forms import RegistroForm


def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_mail(
                subject="Bienvenido a Parcial 2.0",
                message="Tu cuenta fue creada.",
                from_email=settings.EMAIL_SENDER,
                recipient_list=[user.email or settings.EMAIL_SENDER],
                fail_silently=False,
            )
            messages.success(request, "Usuario creado, revisa tu correo.")
            return redirect("login")
    else:
        form = RegistroForm()
    return render(request, "cuentas/registro.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
        messages.error(request, "Credenciales inválidas.")
    return render(request, "cuentas/login.html")


def logout_view(request):
    logout(request)
    return redirect("home")
