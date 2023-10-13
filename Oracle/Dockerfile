FROM python:3.11

RUN apt-get update -y && apt-get install -y libaio1

RUN pip install cx-Oracle

WORKDIR /app

COPY . /app

CMD ["python", "main.py"]