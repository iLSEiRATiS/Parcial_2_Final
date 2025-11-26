from .models import Visita


def registrar_visita(get_response):
    def middleware(request):
        path = request.path
        if not path.startswith("/static/") and not path.startswith("/media/"):
            Visita.objects.create(pagina=path)
        return get_response(request)

    return middleware
