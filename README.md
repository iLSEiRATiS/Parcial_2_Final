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
- **UI**: Bootstrap + estilos propios, navbar y footer.

## Despliegue en Render
Root/workdir: `Parcial2.0`

Build Command:
```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```
Start Command:
```bash
gunicorn parcial20.wsgi --bind 0.0.0.0:$PORT --log-file -
```

Env vars mínimas:
- `DJANGO_SETTINGS_MODULE=parcial20.settings`
- `SECRET_KEY` (cadena segura)
- `DEBUG=False`
- `ALLOWED_HOSTS=tu-dominio.onrender.com`
- `PYTHON_VERSION=3.11.9`
- SMTP (si quieres correos reales):  
  `EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend`  
  `EMAIL_HOST=smtp-relay.brevo.com`  
  `EMAIL_PORT=587`  
  `EMAIL_USE_TLS=True`  
  `EMAIL_USE_SSL=False`  
  `EMAIL_HOST_USER=tu_login_brevo`  
  `EMAIL_HOST_PASSWORD=tu_clave_smtp`  
  `EMAIL_SENDER=remitente_verificado@tudominio.com`

Después del deploy: `python manage.py createsuperuser` (desde la consola de Render si está disponible).

## Rutas principales
- `/` (home) / `/dashboard/`
- `/registro/`, `/login/`, `/logout/`
- `/alumnos/` (CRUD + PDF)
- `/scraper/`
- `/apuntes/`
- `/calendario/`

## Notas
- Si Render bloquea SMTP, usa `EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend` para evitar errores de envío.
- Media/archivos: asegúrate de montar un disco si quieres persistencia en producción.
