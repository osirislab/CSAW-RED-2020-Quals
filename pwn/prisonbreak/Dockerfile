FROM ubuntu:18.04
MAINTAINER N4T_20

RUN apt-get update && apt-get upgrade -y && apt-get install -y apt-utils build-essential socat

RUN useradd -ms /bin/sh prisonbreak

WORKDIR /home/prisonbreak

COPY prisonbreak.c ./
COPY ./Makefile ./
RUN make
COPY ./run.sh ./
COPY flag.txt .

RUN chown -R root:prisonbreak /home/prisonbreak && \
    chmod 750 /home/prisonbreak && \
    chown root:prisonbreak /home/prisonbreak/flag.txt && \
    chmod 555 /home/prisonbreak/prisonbreak && \
    chmod 440 /home/prisonbreak/flag.txt

EXPOSE 8000

USER prisonbreak
CMD ["socat", "-T60", "TCP-LISTEN:8000,reuseaddr,forever,fork", "EXEC:/home/prisonbreak/prisonbreak,stderr"]
