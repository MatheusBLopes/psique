build-image:
	docker build -t psique .

test:
	poetry run pytest -sx psique

lint:
	poetry run pre-commit install && poetry run pre-commit run -a -v
