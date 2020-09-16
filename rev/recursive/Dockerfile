FROM ubuntu:18.04

RUN apt-get update && apt-get -y install socat libc6-dev

RUN useradd -ms /bin/sh recursive

WORKDIR /home/recursive

COPY recursive
COPY flag.txt

RUN chown -R root:recursive /home/recursive && \
    chmod 750  /home/recursive && \
	chown root:recursive /home/recursive/flag.txt && \
    chmod 440 /home/recursive/flag.txt && \
	chown root:recursive /home/recursive/recursive && \
    chmod 750 /home/recursive/recursive
	
EXPOSE 5000
CMD ["socat", "-T60", "TCP-LISTEN:5000,reuseaddr,fork,su=recursive", "EXEC:python3 /home/recursive/recursive,STDERR,pty,echo=0"]