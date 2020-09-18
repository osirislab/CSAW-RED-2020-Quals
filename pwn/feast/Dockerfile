FROM debian:stretch

RUN apt update && apt install -y socat libc6-i386 && rm -rf /var/lib/apt/lists/*

RUN useradd -M chal

WORKDIR /opt/chal

COPY feast .
COPY flag.txt .

RUN chmod 444 flag.txt && chmod 555 feast

USER chal
CMD ["socat", "-T60", "TCP-LISTEN:8000,reuseaddr,fork","EXEC:./feast"]
