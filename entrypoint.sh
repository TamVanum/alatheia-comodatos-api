#!/bin/sh

# Ejecuta las migraciones
python manage.py migrate
python3 manage.py collectstatic --noinput
# Ahora inicia tu aplicación. Por ejemplo, usando gunicorn:
gunicorn application.wsgi:application --bind 0.0.0.0:8000