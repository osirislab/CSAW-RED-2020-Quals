FROM ubuntu:18.04
MAINTAINER K$

RUN apt-get update && apt-get upgrade -y && apt-get install -y apt-utils gcc-multilib build-essential socat

RUN useradd -ms /bin/sh feast

WORKDIR /home/feast

COPY feast.c ./
COPY ./Makefile ./
RUN make
COPY ./run.sh ./
COPY flag.txt .

RUN chown -R root:feast /home/feast && \
    chmod 750 /home/feast && \
    chown root:feast /home/feast/flag.txt && \
    chmod 555 /home/feast/feast && \
    chmod 440 /home/feast/flag.txt

EXPOSE 8000

USER feast
CMD ["socat", "-T60", "TCP-LISTEN:8000,reuseaddr,forever,fork", "EXEC:/home/feast/feast,stderr"]
