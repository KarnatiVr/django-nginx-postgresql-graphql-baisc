FROM python:3.9.0-alpine
WORKDIR /usr/src/app
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip

COPY /requirements.txt requirements.txt
RUN pip install -r requirements.txt

USER root

COPY . .
