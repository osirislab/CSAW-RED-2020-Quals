FROM ubuntu:18.04

RUN apt-get update && apt-get install -y socat

RUN useradd -ms /bin/sh birthday

WORKDIR /home/birthday

COPY birthday .
COPY flag.txt .

RUN chown -R root:birthday /home/birthday && \
    chown root:birthday /home/birthday/flag.txt && \
    chmod 440 /home/birthday/flag.txt && \
    chmod 555 birthday

EXPOSE 8000
USER birthday
CMD ["socat", "-T60", "TCP-LISTEN:8000,reuseaddr,fork","EXEC:/home/birthday/birthday"]
