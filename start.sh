#!/bin/bash

echo "Running database migrations..."
python manage.py migrate

echo "Starting Gunicorn..."
gunicorn blogapp.wsgi:application --bind 0.0.0.0:${PORT}
