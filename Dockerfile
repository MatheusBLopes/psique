FROM 412729474065.dkr.ecr.us-east-1.amazonaws.com/olist/python-api:3.9.6

ARG POETRY_HTTP_BASIC_OLIST_USERNAME
ARG POETRY_HTTP_BASIC_OLIST_PASSWORD

WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-dev

COPY . /app/

EXPOSE 8000

ENTRYPOINT ["gunicorn","-c","gunicorn_config.py","psique.wsgi:application"]
