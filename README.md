# Проект api_yamdb
### Описание
В проекте реализован API интерфейс для получения информации о фильмах и рецензиях к ним.
### Технологии
Python 3.8
Django 3.0.5
### Запуск проекта 
- В папке с файлом manage.py выполните команду:
python manage.py loaddata fixtures.json

- В папке с файлом manage.py выполните команду:

docker-compose up -d --build
docker-compose exec web python manage.py makemigrations users
docker-compose exec web python manage.py migrate users
docker-compose exec web python manage.py makemigrations titles
docker-compose exec web python manage.py migrate titles
docker-compose exec web python manage.py makemigrations reviews
docker-compose exec web python manage.py migrate reviews
docker-compose exec web python manage.py makemigrations tokens
docker-compose exec web python manage.py migrate tokens
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic
### Авторы
mr-Marshanskiy

[![YourActionName Actions Status](https://github.com/mr-Marshanskiy/yamdb_final/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/mr-Marshanskiy/yamdb_final/actions)