FROM python:3.8

RUN mkdir -p /usr/src/app

COPY . /usr/src/app/

WORKDIR /usr/src/app

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT python manage.py runserver 0.0.0.0:8000