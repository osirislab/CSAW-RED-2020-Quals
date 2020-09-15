FROM python:3.8-alpine

WORKDIR /opt/app
COPY requirements.txt requirements.txt

RUN pip3 install -r ./requirements.txt \
  && adduser -D chal

COPY app.py app.py

USER chal
CMD gunicorn -w 8 -b 0.0.0.0:5000 app:app
