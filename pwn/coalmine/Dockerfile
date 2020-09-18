FROM debian:stretch

RUN apt update && apt install -y socat libc6-i386 && rm -rf /var/lib/apt/lists/*

RUN useradd -M chal

WORKDIR /opt/chal

COPY coalmine .
COPY flag.txt .
COPY credits.txt .
COPY birdy.txt .

RUN chmod 444 flag.txt \
  && chmod 444 credits.txt \
  && chmod 444 birdy.txt \
  && chmod 555 coalmine

EXPOSE 5000

USER chal
CMD ["socat", "-T60", "TCP-LISTEN:5000,reuseaddr,fork","EXEC:./coalmine"]
