FROM python:3.8

ENV PYTHONUNBUFFERED=1

COPY . /django

WORKDIR /django

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt
