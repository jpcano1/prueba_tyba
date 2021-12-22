FROM python:3.9.7-slim

MAINTAINER Juan Pablo Cano <cano.juanpablo123@gmail.com>

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -yy libpq-dev build-essential && \
    pip install -r requirements.txt \

COPY . .
CMD gunicorn --bind=0.0.0.0:5000 --log-level=DEBUG -w=4 --timeout=20 'base_app:app'