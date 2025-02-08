FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt upgrade -y && apt install git -y

WORKDIR /code

COPY . /code/

RUN pip install -r requirements.txt

CMD python3 manage.py runserver 0.0.0.0:8000

