FROM ubuntu:18.04

RUN apt-get update && apt-get -y install python3-pip socat

RUN useradd -ms /bin/sh babyrsa

WORKDIR /home/babyrsa

COPY rsa.py

RUN chown -R root:babyrsa /home/babyrsa && \
    chmod 750  /home/babyrsa && \
	chown root:babyrsa /home/babyrsa/rsa.py && \
    chmod 750 /home/babyrsa/rsa.py
	
EXPOSE 5000
CMD ["socat", "-T60", "TCP-LISTEN:5000,reuseaddr,fork,su=babyrsa", "EXEC:python3 /home/babyrsa/rsa.py,STDERR,pty,echo=0"]