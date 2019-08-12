#!/bin/bash

echo "export DJANGO_SETTINGS_MODULE={{ project_name }}.settings.base"

echo "Setting: ${DJANGO_SETTINGS_MODULE}"

# Migrate DB
echo "Migrate DB"
python manage.py migrate

echo "Run server..."
# python manage.py runserver 0.0.0.0:8000 --verbosity 0
gunicorn weather.wsgi --bind 0.0.0.0:8000 --workers 1 --threads 1