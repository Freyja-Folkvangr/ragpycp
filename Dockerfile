FROM python:3.8-slim

RUN mkdir -p /usr/src/app

COPY . /usr/src/app/

WORKDIR /usr/src/app

RUN pip install -r requirements.txt

EXPOSE 8000

ENV DATABASE_HOST=""
ENV DATABASE_NAME=""
ENV DATABASE_USER=""
ENV DATABASE_PASSWORD=""
ENV DATABASE_PORT=""
ENV HOST="freyja-ro.xyz"

ENTRYPOINT python manage.py runserver 0.0.0.0:8000