FROM ubuntu:18.04

RUN apt-get update && apt-get install -y socat

RUN useradd -ms /bin/sh worstcodeever

WORKDIR /home/worstcodeever

COPY worstcodeever .
COPY flag.txt .

RUN chown -R root:worstcodeever /home/worstcodeever && \
    chown root:worstcodeever /home/worstcodeever/flag.txt && \
    chmod 440 /home/worstcodeever/flag.txt && \
    chmod 555 worstcodeever

EXPOSE 8000
USER worstcodeever
CMD ["socat", "-T60", "TCP-LISTEN:8000,reuseaddr,fork","EXEC:/home/worstcodeever/worstcodeever"]
