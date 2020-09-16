FROM ubuntu:18.04

RUN apt-get update && apt-get -y install python3-pip socat

RUN useradd -ms /bin/sh teenrsa

WORKDIR /home/teenrsa

COPY rsa.py

RUN chown -R root:teenrsa /home/teenrsa && \
    chmod 750  /home/teenrsa && \
	chown root:teenrsa /home/teenrsa/rsa.py && \
    chmod 750 /home/teenrsa/rsa.py
	
EXPOSE 5000
CMD ["socat", "-T60", "TCP-LISTEN:5000,reuseaddr,fork,su=teenrsa", "EXEC:python3 /home/teenrsa/rsa.py,STDERR,pty,echo=0"]