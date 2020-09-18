FROM ubuntu:18.04
MAINTAINER N4T_20

RUN apt-get update && apt-get upgrade -y && apt-get install -y apt-utils gcc-multilib build-essential socat

RUN useradd -ms /bin/sh coalmine

WORKDIR /home/coalmine

COPY coalmine.c ./
COPY ./Makefile ./
RUN make
COPY ./run.sh ./
COPY birdy.txt .
COPY flag.txt .
COPY credits.txt .

RUN chown -R root:coalmine /home/coalmine && \
    chmod 750 /home/coalmine && \
    chown root:coalmine /home/coalmine/flag.txt && \
    chmod 555 /home/coalmine/coalmine && \
    chmod 440 /home/coalmine/flag.txt

EXPOSE 8000

USER coalmine
CMD ["socat", "-T60", "TCP-LISTEN:8000,reuseaddr,forever,fork", "EXEC:/home/coalmine/coalmine,stderr"]


