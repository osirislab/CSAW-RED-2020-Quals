FROM debian:stretch

RUN apt update && apt install -y socat libc6-i386 libssl-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /home/

COPY whack200.py .

RUN chmod 555 whack200.py

EXPOSE 5000

USER chal
CMD ["socat", "-T60", "TCP-LISTEN:5000,reuseaddr,fork","EXEC:./whack200.py"]
