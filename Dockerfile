FROM python:3.9-slim

RUN mkdir -p /usr/src/app

COPY . /usr/src/app/

WORKDIR /usr/src/app

RUN apt update \
    && apt install -y --no-install-recommends gcc default-mysql-client default-libmysqlclient-dev \
    && pip install -r requirements.txt \
    && apt purge -y --auto-remove gcc

EXPOSE 8000

ENV DATABASE_HOST=""
ENV DATABASE_NAME=""
ENV DATABASE_USER=""
ENV DATABASE_PASSWORD=""
ENV DATABASE_PORT=""
ENV HOST="freyja-ro.xyz"
ENV DJANGO_SETTINGS_MODULE="ragcp.settings"
ENV GITHUB_TOKEN=""
ENV RAGCP_REPO_NAME="ragpycp"
ENV RATHENA_REPO_NAME="rathena"

ENTRYPOINT python manage.py runserver 0.0.0.0:8000
