newapp:
	python manage.py startapp $(name)

runserver:
	python manage.py runserver

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

help:
	python manage.py --help

createsuperuser:
	python manage.py createsuperuser

fill_db:
	python manage.py fill_db

unfill_db:
	python manage.py unfill_db

db_init:
	make migrate
	make fill_db


