FROM ubuntu:18.04
MAINTAINER N4T_20 and K$

RUN apt-get update && apt-get upgrade -y && apt-get install -y apt-utils gcc-multilib build-essential socat

RUN useradd -ms /bin/sh actually_not_guessy

WORKDIR /home/actually_not_guessy

COPY actually_not_guessy.c ./
COPY ./Makefile ./
RUN make
COPY flag.txt .

RUN chown -R root:actually_not_guessy /home/actually_not_guessy && \
    chmod 750 /home/actually_not_guessy && \
    chown root:actually_not_guessy /home/actually_not_guessy/flag.txt && \
    chmod 555 /home/actually_not_guessy/actually_not_guessy && \
    chmod 440 /home/actually_not_guessy/flag.txt

EXPOSE 8000

USER actually_not_guessy
CMD ["socat", "-T60", "TCP-LISTEN:8000,reuseaddr,forever,fork", "EXEC:/home/actually_not_guessy/actually_not_guessy,stderr"]