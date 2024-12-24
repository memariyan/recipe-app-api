# recipe-app-api
Recipe API Project

setup django :
docker compose run --rm app sh -c "django-admin startproject app ."

setup core module :
docker compose run --rm app sh -c "django-admin startapp core"

test :
docker compose run --rm app sh -c "python manage.py test"

migration :
docker compose run --rm app sh -c "python manage.py makemigrations"

create superuser :
docker compose run --rm app sh -c "python manage.py createsuperuser"

check lint:
docker compose run --rm app sh -c "flake8"

run:
docker compose up
