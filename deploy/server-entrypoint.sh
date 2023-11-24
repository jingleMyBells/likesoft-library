#!/bin/sh

until cd /app
do
    echo "Waiting for app dir exists..."
done


until python manage.py migrate
do
    echo "Waiting for db to be ready, even with healthcheck"
    sleep 2
done


python manage.py collectstatic --noinput

gunicorn library.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4

