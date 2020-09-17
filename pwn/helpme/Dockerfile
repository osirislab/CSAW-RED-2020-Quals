FROM alpine:3.12

RUN apk add --update --no-cache socat

RUN adduser -D chal

WORKDIR /opt/chal

COPY helpme .
COPY flag.txt .

RUN chmod 444 flag.txt && chmod 555 helpme

EXPOSE 8000

USER chal
CMD ["socat", "-T60", "TCP-LISTEN:8000,reuseaddr,fork","EXEC:./helpme"]
