FROM ubuntu:18.04
MAINTAINER N4T_20

RUN apt-get update && apt-get upgrade -y && apt-get install -y apt-utils build-essential socat

RUN useradd -ms /bin/sh partycreation

WORKDIR /home/partycreation

COPY partycreation.c ./
COPY ./Makefile ./
RUN make
COPY ./run.sh ./
COPY flag.txt .

RUN chown -R root:partycreation /home/partycreation && \
    chmod 750 /home/partycreation && \
    chown root:partycreation /home/partycreation/flag.txt && \
    chmod 555 /home/partycreation/partycreation && \
    chmod 440 /home/partycreation/flag.txt

EXPOSE 8000

USER partycreation
CMD ["socat", "-T60", "TCP-LISTEN:8000,reuseaddr,forever,fork", "EXEC:/home/partycreation/partycreation,stderr"]
