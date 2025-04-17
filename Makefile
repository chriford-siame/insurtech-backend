
migrate:
	@python3 manage.py migrate

migrations:
	@python3 manage.py makemigrations

collectstatic:
	@python3 manage.py collectstatic --no-input

superuser:
	@python3 manage.py createsuperuser

runserver:
	@python3 manage.py runserver 8000

django-shell:
	@python3 manage.py shell

build:
	@docker compose build

start:
	@docker compose up -d

start-live:
	@docker compose up

stop:
	@docker compose down

kill:
	@docker compose down -v

fixtures:
	@python manage.py loaddata categories.json
	@python manage.py loaddata products.json
	@python manage.py loaddata product_images.json
