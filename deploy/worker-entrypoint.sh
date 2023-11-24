#!/bin/sh

until cd /app
do
    echo "Waiting for app dir exists..."
done

celery -A library worker --loglevel=info