FROM ubuntu:18.04

RUN apt-get update && apt-get install -y socat

RUN useradd -ms /bin/sh concrete_trap

WORKDIR /home/concrete_trap

COPY concrete_trap .
COPY flag.txt .

RUN chown -R root:concrete_trap /home/concrete_trap && \
    chown root:concrete_trap /home/concrete_trap/flag.txt && \
    chmod 440 /home/concrete_trap/flag.txt && \
    chmod 555 concrete_trap

EXPOSE 8000
USER concrete_trap
CMD ["socat", "-T60", "TCP-LISTEN:8000,reuseaddr,fork","EXEC:/home/concrete_trap/concrete_trap"]
