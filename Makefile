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