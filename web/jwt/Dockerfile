FROM python:3.8-alpine

WORKDIR /opt/app

COPY requirements.txt requirements.txt

RUN pip3 install -r ./requirements.txt \
  && adduser -HD www \
  && chown www:www -R /opt/app

USER www

COPY . .

CMD gunicorn -b 0.0.0.0:5000 -w 8 src:app

