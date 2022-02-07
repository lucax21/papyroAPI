FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY /requirements.txt . 

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .
