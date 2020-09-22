FROM debian:stretch

RUN apt update && apt install -y socat libc6-i386 libssl-dev && rm -rf /var/lib/apt/lists/*

RUN useradd -M chal

WORKDIR /opt/chal

COPY fabricator .
COPY flag.txt .

RUN chmod 444 flag.txt && chmod 555 fabricator

EXPOSE 5000

USER chal
CMD ["socat", "-T60", "TCP-LISTEN:5000,reuseaddr,fork","EXEC:./fabricator"]