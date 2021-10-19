build-image:
	docker build -t psique .

test:
	poetry run pytest -sx psique

lint:
	poetry run pre-commit install && poetry run pre-commit run -a -v

runserver:
	python ./psique/manage.py runserver

make migrations:
	python ./psique/manage.py makemigrations

make migrate:
	python ./psique/manage.py migrate
