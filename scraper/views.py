import requests
from bs4 import BeautifulSoup
from django.shortcuts import render


def buscar(request):
    query = request.GET.get("q", "").strip()
    resultados = []
    error = ""
    if query:
        try:
            url = "https://es.wikipedia.org/w/index.php"
            resp = requests.get(url, params={"search": query}, timeout=5)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, "html.parser")
                titulo = soup.find("h1").get_text() if soup.find("h1") else "Sin titulo"
                parrafos = soup.find_all("p")
                snippets = [p.get_text(strip=True) for p in parrafos[:3] if p.get_text(strip=True)]
                resultados.append({"titulo": titulo, "snippets": snippets, "url": resp.url})
                if not snippets:
                    error = "No se encontraron parrafos en la pagina."
            else:
                error = f"Respuesta inesperada: {resp.status_code}"
        except Exception as exc:  # pragma: no cover - manejo simple
            error = f"Error al buscar: {exc}"
    return render(request, "scraper/buscar.html", {"resultados": resultados, "query": query, "error": error})
