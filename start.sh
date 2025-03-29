#!/bin/bash

# Statik dosyaları topla
python manage.py collectstatic --noinput

# Veritabanı migrasyonlarını çalıştır
python manage.py migrate

# Django projesini Gunicorn ile başlat
gunicorn blogapp.wsgi:application --bind 0.0.0.0:8000
