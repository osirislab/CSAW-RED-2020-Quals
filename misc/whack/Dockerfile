FROM debian:stretch

RUN apt-get update && apt-get install -y python3 python3-pip 
RUN apt-get install -y socat && rm -rf /var/lib/apt/lists/*

RUN useradd -M cha1

WORKDIR /opt/cha1

COPY whack200.py .

RUN chmod 555 whack200.py

EXPOSE 5000

CMD ["socat", "-T60", "TCP-LISTEN:5000,reuseaddr,fork","EXEC:/usr/bin/python3 /opt/cha1/whack200.py"]
