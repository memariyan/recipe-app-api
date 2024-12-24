# recipe-app-api
Recipe API Project

setup django :
docker compose run --rm app sh -c "django-admin startproject app ."

test :
docker compose run --rm app sh -c "python manage.py test"

check lint:
docker compose run --rm app sh -c "flake8"

run:
docker compose up
