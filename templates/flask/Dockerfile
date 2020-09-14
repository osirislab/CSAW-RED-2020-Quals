FROM python:3.8

WORKDIR /opt/app
COPY requirements.txt requirements.txt

RUN pip3 install -r ./requirements.txt \
  && useradd -M chal

COPY app.py app.py

RUN mv flag.txt /flag.txt \
  && chmod 444 /flag.txt \
  && chmod 444 ./app.py
USER chal

CMD gunicorn -w 8 -b 0.0.0.0:5000 app:app
