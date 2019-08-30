FROM python:3.7.2-stretch

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD flask db migrate
CMD flask db upgrade
CMD ["uwsgi", "uwsgi.ini"]