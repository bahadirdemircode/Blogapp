#!/bin/bash
python manage.py migrate
gunicorn blogapp.wsgi:application --bind 0.0.0.0:8000
