pip install Django

python -m django --version

django-admin startproject shoppy

cd shoppy

python manage.py runserver

localhost:8000

### if models are updated

python manage.py makemigrations

python manage.py migrate

### Create Super User

python manage.py createsuperuser

username: admin

password: 123123