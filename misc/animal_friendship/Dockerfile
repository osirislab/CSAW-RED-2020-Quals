FROM debian:stretch

RUN apt-get update && apt-get install -y python3 python3-pip 
RUN apt-get install -y socat && rm -rf /var/lib/apt/lists/*

RUN useradd -M chal

WORKDIR /opt/chal

COPY animal_friendship.py .

RUN chmod 555 animal_friendship.py

EXPOSE 5000

CMD ["socat", "-T60", "TCP-LISTEN:5000,reuseaddr,fork","EXEC:/usr/bin/python3 /opt/chal/animal_friendship.py"]
