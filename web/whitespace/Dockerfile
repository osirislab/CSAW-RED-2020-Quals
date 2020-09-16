FROM python:3.8-alpine

WORKDIR /opt/app
COPY requirements.txt requirements.txt

RUN apk add --update --no-cache supervisor \
  && pip3 install -r ./requirements.txt \
  && adduser -DH www

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY app.py app.py
COPY flag.txt flag.txt
COPY templates templates

RUN chown www:www -R .

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
