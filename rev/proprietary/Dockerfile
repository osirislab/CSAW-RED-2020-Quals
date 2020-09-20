FROM ubuntu:18.04

RUN apt-get update && apt-get install -y socat

RUN useradd -ms /bin/sh prop_remote

WORKDIR /home/prop_remote

COPY prop_remote .

RUN chown -R root:prop_remote /home/prop_remote && \
    chmod 555 prop_remote

USER prop_remote
CMD ["socat", "-T60", "TCP-LISTEN:5000,reuseaddr,fork","EXEC:/home/prop_remote/prop_remote"]
