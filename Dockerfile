FROM python:3.9

WORKDIR /code

COPY /requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080","--reload" ,"--reload-dir=src"]