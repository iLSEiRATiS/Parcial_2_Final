from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.conf import settings

from .forms import ApunteForm
from .models import Apunte


@login_required
def lista_apuntes(request):
    apuntes = Apunte.objects.filter(usuario=request.user)
    return render(request, "apuntes/lista.html", {"apuntes": apuntes})


@login_required
def crear_apunte(request):
    if request.method == "POST":
        form = ApunteForm(request.POST)
        if form.is_valid():
            apunte = form.save(commit=False)
            apunte.usuario = request.user
            apunte.save()
            messages.success(request, "Apunte guardado.")
            destino = request.user.email or settings.EMAIL_SENDER
            send_mail(
                subject=f"Nuevo apunte: {apunte.titulo}",
                message=apunte.contenido,
                from_email=settings.EMAIL_SENDER,
                recipient_list=[destino],
                fail_silently=False,
            )
            return redirect("apuntes")
    else:
        form = ApunteForm()
    return render(request, "apuntes/form.html", {"form": form, "titulo": "Nuevo apunte"})


@login_required
def detalle_apunte(request, pk):
    apunte = Apunte.objects.filter(usuario=request.user).filter(pk=pk).first()
    if not apunte:
        return redirect("apuntes")
    return render(request, "apuntes/detalle.html", {"apunte": apunte})


@login_required
def editar_apunte(request, pk):
    apunte = Apunte.objects.filter(usuario=request.user).filter(pk=pk).first()
    if not apunte:
        return redirect("apuntes")
    if request.method == "POST":
        form = ApunteForm(request.POST, instance=apunte)
        if form.is_valid():
            form.save()
            return redirect("detalle_apunte", pk=pk)
    else:
        form = ApunteForm(instance=apunte)
    return render(request, "apuntes/form.html", {"form": form, "titulo": "Editar apunte"})
