FROM python:3.9-slim

RUN mkdir /app

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY cadastral_service/ /app/cadastral_service
COPY extraservice/ /app/extraservice

WORKDIR /app

CMD ["sh", "-c", "python3 /app/cadastral_service/manage.py runserver 0:8000 & python3 /app/extraservice/manage.py runserver 0:8080"]
