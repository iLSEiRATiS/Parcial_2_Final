import requests
from bs4 import BeautifulSoup
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render


USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"


@login_required
def scraper_view(request):
    palabra = request.GET.get("q", "").strip()
    resultados = []
    if palabra:
        url = "https://es.wikipedia.org/w/index.php"
        try:
            resp = requests.get(
                url,
                params={"search": palabra},
                headers={"User-Agent": USER_AGENT},
                timeout=5,
            )
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, "html.parser")
                textos = []
                for p in soup.select("p"):
                    raw = p.get_text(" ", strip=True)
                    clean = " ".join(raw.split())
                    if clean:
                        textos.append(clean)
                resultados = textos[:5]
                destino = request.user.email or settings.EMAIL_SENDER
                send_mail(
                    subject=f"Scraper resultados para {palabra}",
                    message="\n\n".join(resultados) or "Sin resultados",
                    from_email=settings.EMAIL_SENDER,
                    recipient_list=[destino],
                    fail_silently=False,
                )
                messages.success(request, "Resultados enviados por correo.")
            else:
                messages.error(request, f"Status {resp.status_code}: no se pudo acceder.")
        except Exception as exc:  # pragma: no cover
            messages.error(request, f"Error: {exc}")
    return render(request, "scraper/scraper.html", {"palabra": palabra, "resultados": resultados})
