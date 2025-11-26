from django.db.models import Count
from django.db.models.functions import TruncDate, TruncHour
from django.shortcuts import render
from django.utils import timezone

from .models import Visita


def dashboard(request):
    visitas_por_dia = (
        Visita.objects.annotate(fecha_dia=TruncDate("fecha"))
        .values("fecha_dia")
        .annotate(total=Count("id"))
        .order_by("fecha_dia")
    )
    paginas_populares = (
        Visita.objects.values("pagina")
        .annotate(total=Count("id"))
        .order_by("-total")[:10]
    )
    hoy = timezone.localdate()
    visitas_hora = (
        Visita.objects.filter(fecha__date=hoy)
        .annotate(hora=TruncHour("fecha"))
        .values("hora")
        .annotate(total=Count("id"))
        .order_by("hora")
    )
    total_visitas = Visita.objects.count()
    return render(
        request,
        "estadisticas/dashboard.html",
        {
            "visitas_labels": [v["fecha_dia"].strftime("%Y-%m-%d") for v in visitas_por_dia],
            "visitas_data": [v["total"] for v in visitas_por_dia],
            "paginas_labels": [p["pagina"] for p in paginas_populares],
            "paginas_data": [p["total"] for p in paginas_populares],
            "hora_labels": [h["hora"].strftime("%H:%M") for h in visitas_hora],
            "hora_data": [h["total"] for h in visitas_hora],
            "total_visitas": total_visitas,
        },
    )
