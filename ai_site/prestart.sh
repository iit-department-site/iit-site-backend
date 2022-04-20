#!/usr/bin/env python

python manage.py makemigrations

python manage.py migrate

python manage.py collectstatic

uwsgi --ini ai_site.ini
