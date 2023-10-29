# see Python versions on https://hub.docker.com/_/python
FROM python:3.11.6

WORKDIR /app/

RUN pip install poetry uvicorn==0.23.2
RUN poetry config virtualenvs.create false


COPY assets assets
COPY README.md .

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install --no-root

COPY tuto_docker tuto_docker
RUN poetry install --only-root

CMD ["uvicorn", "tuto_docker:app", "--host", "0.0.0.0", "--port", "80"]