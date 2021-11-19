FROM python:3-slim

RUN pip3 install poetry
RUN poetry config virtualenvs.create false

RUN mkdir /listener
COPY ./listener /listener
COPY pyproject.toml /listener/

WORKDIR /listener
RUN poetry install --no-dev --no-root
