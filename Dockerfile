FROM python:3

ENV PYTHONUNBUFFERD 1

RUN mkdir /am_test
WORKDIR /am_test
COPY . /am_test/

RUN pip install -r requirements.txt