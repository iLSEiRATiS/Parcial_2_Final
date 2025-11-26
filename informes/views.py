from io import BytesIO

from django.contrib import messages
from django.http import FileResponse
from django.shortcuts import get_object_or_404, redirect, render
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from .forms import ReporteForm
from .models import Reporte


def informes_view(request):
    if request.method == "POST":
        form = ReporteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Reporte guardado.")
            return redirect("informes")
        messages.error(request, "Revisa los datos del formulario.")
    else:
        form = ReporteForm()
    informes = Reporte.objects.all().order_by("-fecha")
    return render(request, "informes/lista.html", {"form": form, "informes": informes})


def reporte_pdf(request, pk):
    reporte = get_object_or_404(Reporte, pk=pk)
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.setFont("Helvetica-Bold", 16)
    p.drawString(72, 750, reporte.nombre)
    p.setFont("Helvetica", 12)
    p.drawString(72, 730, f"Fecha: {reporte.fecha}")
    p.drawString(72, 700, "Contenido:")
    text_obj = p.beginText(72, 680)
    for line in reporte.contenido.splitlines():
        text_obj.textLine(line)
    p.drawText(text_obj)
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f"reporte_{reporte.id}.pdf")
