bash:
	docker-compose run --rm backend bash

build:
	docker-compose build

createsuperuser:
	docker-compose run --rm backend python manage.py createsuperuser

makemigrations:
	docker-compose run --rm backend python manage.py makemigrations

migrate:
	docker-compose run --rm backend python manage.py migrate

run:
	docker-compose up -d
