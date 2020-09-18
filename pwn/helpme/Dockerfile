FROM debian:stretch

RUN apt update && apt install -y socat && rm -rf /var/lib/apt/lists/*

RUN useradd -M helpme

WORKDIR /opt/chal

COPY helpme .
COPY flag.txt .

RUN chmod 444 flag.txt && chmod 555 helpme
RUN chown -R root:helpme /opt/chal && \
    chown root:helpme /opt/chal/flag.txt && \
    chmod 440 /opt/chal/flag.txt && \
    chmod 555 helpme

USER helpme
CMD ["socat", "-T60", "TCP-LISTEN:5000,reuseaddr,fork","EXEC:./helpme"]
