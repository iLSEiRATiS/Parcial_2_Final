from io import BytesIO

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from .forms import AlumnoForm
from .models import Alumno


@login_required
def dashboard(request):
    total = Alumno.objects.filter(usuario=request.user).count()
    recientes = Alumno.objects.filter(usuario=request.user).order_by("-creado")[:5]
    return render(request, "alumnos/dashboard.html", {"total": total, "recientes": recientes})


@login_required
def lista_alumnos(request):
    alumnos = Alumno.objects.filter(usuario=request.user).order_by("-creado")
    return render(request, "alumnos/lista.html", {"alumnos": alumnos})


@login_required
def crear_alumno(request):
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.usuario = request.user
            alumno.save()
            messages.success(request, "Alumno creado.")
            return redirect("alumnos")
    else:
        form = AlumnoForm()
    return render(request, "alumnos/form.html", {"form": form, "titulo": "Nuevo alumno"})


@login_required
def detalle_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk, usuario=request.user)
    return render(request, "alumnos/detalle.html", {"alumno": alumno})


@login_required
def editar_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk, usuario=request.user)
    if request.method == "POST":
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            messages.success(request, "Alumno actualizado.")
            return redirect("alumnos")
    else:
        form = AlumnoForm(instance=alumno)
    return render(request, "alumnos/form.html", {"form": form, "titulo": "Editar alumno"})


@login_required
def eliminar_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk, usuario=request.user)
    if request.method == "POST":
        alumno.delete()
        messages.info(request, "Alumno eliminado.")
        return redirect("alumnos")
    return render(request, "alumnos/confirmar_eliminar.html", {"alumno": alumno})


@login_required
def enviar_pdf(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk, usuario=request.user)
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.setFont("Helvetica-Bold", 16)
    p.drawString(72, 750, f"Alumno: {alumno.nombre}")
    p.setFont("Helvetica", 12)
    p.drawString(72, 730, f"Carrera: {alumno.carrera}")
    p.drawString(72, 710, f"Legajo: {alumno.legajo}")
    fecha_val = alumno.creado
    if not timezone.is_naive(fecha_val):
        fecha_val = timezone.localtime(fecha_val)
    p.drawString(72, 690, f"Fecha: {fecha_val.strftime('%Y-%m-%d %H:%M')}")
    p.showPage()
    p.save()
    buffer.seek(0)
    destino = request.user.email or settings.EMAIL_HOST_USER
    email = EmailMessage(
        subject=f"Ficha alumno: {alumno.nombre}",
        body="Adjunto PDF del alumno.",
        from_email=settings.EMAIL_SENDER,
        to=[destino],
    )
    email.attach(f"alumno_{alumno.id}.pdf", buffer.read(), "application/pdf")
    try:
        email.send(fail_silently=False)
        messages.success(request, "PDF enviado por correo.")
    except Exception as exc:  # pragma: no cover
        messages.error(request, f"No se pudo enviar el correo: {exc}")
    return redirect("alumnos")
