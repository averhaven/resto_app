# syntax=docker/dockerfile:1

FROM python:3.9

WORKDIR /resto_app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV  FLASK_APP=resto

CMD python3 -m flask run --host=0.0.0.0