#FROM ubuntu:latest
#LABEL authors="ismae"
#
#ENTRYPOINT ["top", "-b"]

FROM python:3.8

WORKDIR /app
COPY . /app

RUN pip install -r required.txt
EXPOSE 80
ENV NAME world
CMD ["python", "app.py"]