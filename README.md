# Parcial 2.0 – Plataforma académica en Django

Proyecto Django con autenticación, gestión de alumnos, generación de PDF, scraper educativo, apuntes, calendario de eventos y despliegue listo para Render.

## Requisitos
- Python 3.11
- pip
- (Opcional) Base de datos Postgres en producción

## Instalación local
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Variables útiles (local):
- `DJANGO_SETTINGS_MODULE=parcial20.settings`
- `DEBUG=True`
- `ALLOWED_HOSTS=127.0.0.1,localhost`
- `EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend` (o SMTP real si quieres enviar correos)

## Funcionalidades
- **Auth**: registro, login/logout, correo de bienvenida.
- **Dashboard**: acceso rápido a apps.
- **Alumnos**: CRUD, envío de PDF por correo.
- **Scraper**: búsqueda en Wikipedia, muestra snippets, envía resultados por correo.
- **Apuntes**: notas personales.
- **Calendario**: eventos de parciales/presentaciones.
- **UI**: Bootstrap + estilos propios, navbar y footer
