#!/bin/bash

# # Collect static files
# echo "Collect static files"
# python manage.py collectstatic --noinput

# Make database migrations
echo "Make database migrations"
python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

echo "Install Neo4j Labels"
python manage.py install_labels

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000