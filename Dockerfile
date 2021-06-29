# pull official base image
FROM python:3.8-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps
RUN apk add --virtual build-deps --no-cache gcc python3-dev musl-dev zlib-dev postgresql-dev jpeg-dev
RUN apk add postgresql zlib jpeg
RUN pip install psycopg2 Pillow==8.0.1
# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# add and run as non-root user
RUN usuario01 -D usuario01
USER usuario01

# run gunicorn
CMD gunicorn hello_django.wsgi:application --bind 0.0.0.0:$PORT