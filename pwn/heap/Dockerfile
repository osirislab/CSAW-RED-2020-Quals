FROM ubuntu:18.04

RUN apt-get update && apt-get install -y socat

RUN useradd -ms /bin/sh heap

WORKDIR /home/heap

COPY heap .
COPY flag.txt .

RUN chown -R root:heap /home/heap && \
    chown root:heap /home/heap/flag.txt && \
    chmod 440 /home/heap/flag.txt && \
    chmod 555 heap

EXPOSE 8000
USER heap
CMD ["socat", "-T60", "TCP-LISTEN:8000,reuseaddr,fork","EXEC:/home/heap/heap"]
