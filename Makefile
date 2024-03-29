newapp:
	python manage.py startapp $(name)
	# make newapp name=<app_name>

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

clear_db:
	python manage.py unfill_db

db_init:
	docker compose up -d pg
	timeout 5 make migrate
	make fill_db

send_email:
	python manage.py send_email

run_workers:
	python manage.py rqworker default
