#!/bin/bash

echo "Setting: ${DJANGO_SETTINGS_MODULE}"

# Migrate DB
echo "Migrate DB"
python manage.py migrate

if test -n "$IS_PREVIEW"
then
    echo "Creating a superuser for Preview:"
    echo "  ID) test"
    echo "  PW) test"
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('test', 'test@intellisys.co.kr', 'test')" | python manage.py shell
fi

echo "Run server..."
gunicorn {{ project_name }}.wsgi --bind 0.0.0.0:8000 --workers 2 --threads 2
