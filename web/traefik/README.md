# Traefik

## Overview

Traefik is a reverse proxy.

![alt text](https://docs.traefik.io/assets/img/traefik-architecture.png)

Reverse proxies will listen on a port, and forward http requests based on the 
`Host` header. All this challenge asks you to do is realize that you can
make the `Host` header whatever the hell you want. Just by setting the 
header to flag, you'll be telling traefik to route the request to the flag
container (theirby getting the flag).

This challenge would require 3 containers, one of which would need the docker
socket mounted (which i really really dont like). Due to this, I'm deploying it
much much simpler by just having a single container that looks for the correct
headers and returns the flag.

## Solution

All you need to do is send an http request and set the host header to `flag`.

```bash
curl http://<host>:<ip>/ -H "Host:flag"
```
