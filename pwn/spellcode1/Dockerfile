FROM ubuntu:18.04
MAINTAINER N4T_20

RUN apt-get update && apt-get upgrade -y && apt-get install -y apt-utils gcc-multilib build-essential socat

RUN useradd -ms /bin/sh spellcode1

WORKDIR /home/spellcode1

COPY level_1_spellcode.c ./
COPY ./Makefile ./
RUN make
COPY ./run.sh ./
COPY flag.txt .

RUN chown -R root:spellcode1 /home/spellcode1 && \
    chmod 750 /home/spellcode1 && \
    chown root:spellcode1 /home/spellcode1/flag.txt && \
    chmod 555 /home/spellcode1/level_1_spellcode && \
    chmod 440 /home/spellcode1/flag.txt

EXPOSE 8000

USER spellcode1
CMD ["socat", "-T60", "TCP-LISTEN:8000,reuseaddr,forever,fork", "EXEC:/home/spellcode1/level_1_spellcode,stderr"]
