FROM python:3.8-alpine

WORKDIR /opt/app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
# EXPOSE 80

CMD gunicorn -b "0.0.0.0:5000" -w 10 rev-proxy:app
