FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /papyroAPI

COPY ./requirements.txt /papyroAPI/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /papyroAPI/requirements.txt

COPY ./src /papyroAPI/src

