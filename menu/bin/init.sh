#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata initial_data.json