FROM python:3.7.2-stretch

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

RUN chmod u+x ./wait-for-it.sh
RUN chmod u+x ./entrypoint.sh