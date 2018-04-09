#!/bin/bash

./wait_for_it.sh psqldb:5432 -- echo "Postgres is up."
./wait_for_it.sh neo4jdb:7687 -- echo "Neo4j db is up."
./wait_for_it.sh neo4jdb:7474 -- echo "Neo4j service is up."

# # Collect static files
# echo "Collect static files"
# python manage.py collectstatic --noinput

# Make database migrations
echo "Make database migrations"
python manage.py makemigrations

./wait_for_it.sh psqldb:5432 -- echo "Postgres is up."

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

echo "Install Neo4j Labels"
python manage.py install_labels

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000