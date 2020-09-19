FROM ubuntu:18.04

RUN apt-get update && apt-get install -y socat

RUN useradd -ms /bin/sh spaghetti

WORKDIR /home/spaghetti

COPY spaghetti .
COPY flag.txt .

RUN chown -R root:spaghetti /home/spaghetti && \
    chown root:spaghetti /home/spaghetti/flag.txt && \
    chmod 440 /home/spaghetti/flag.txt && \
    chmod 555 spaghetti

USER spaghetti
CMD ["socat", "-T60", "TCP-LISTEN:5000,reuseaddr,fork","EXEC:/home/spaghetti/spaghetti"]
