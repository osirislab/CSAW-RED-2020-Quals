FROM ubuntu:18.04

RUN apt-get update && apt-get install -y socat

RUN useradd -ms /bin/sh proprietary

WORKDIR /home/proprietary

COPY proprietary .

RUN chown -R root:proprietary /home/proprietary && \
    chown root:concrete_trap /home/proprietary/flag.txt && \
    chmod 440 /home/proprietary/flag.txt && \
    chmod 555 proprietary

USER proprietary
CMD ["socat", "-T60", "TCP-LISTEN:5000,reuseaddr,fork","EXEC:/home/proprietary/proprietary"]
