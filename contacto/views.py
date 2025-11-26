from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactoForm


def contacto_view(request):
    enviado = False
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            send_mail(
                subject=f"Contacto de {data['nombre']}",
                message=data["mensaje"],
                from_email=data["email"],
                recipient_list=[settings.EMAIL_HOST_USER],
            )
            enviado = True
    else:
        form = ContactoForm()
    return render(request, "contacto/contacto.html", {"form": form, "enviado": enviado})
