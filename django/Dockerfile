FROM python:3.9.0-alpine
WORKDIR /usr/src/app
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip

COPY /requirements.txt requirements.txt
RUN pip install -r requirements.txt

USER root

COPY . .

CMD python manage.py collectstatic --no-input && python manage.py migrate && gunicorn app.wsgi:application --bind 0.0.0.0:8000