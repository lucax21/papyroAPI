FROM python:3.10

WORKDIR /papyroAPI

COPY ./requirements.txt /papyroAPI/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /papyroAPI/requirements.txt

COPY ./src /papyroAPI/src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
