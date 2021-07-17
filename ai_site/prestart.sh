#!/usr/bin/env python

sleep 10;
python manage.py migrate

sleep 10;

python manage.py runserver 0.0.0.0:8000